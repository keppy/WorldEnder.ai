import useSWR from "swr";
import { config } from "./config";

export const postScenarioNewUri = () => "/scenario/new";
export const getScenarioUri = (id: string) => `/scenario/${id}`;
export const postScenarioChooseUri = (id: string) => `/scenario/${id}/choose`;
export const postScenarioTickUri = (id: string) => `/scenario/${id}/tick`;
export const postGamePlan = (id: string) => `/gameplan/${id}`;
export const postQuestion = (id: string) => `/question/${id}`;

interface ApiErrorBody {
  message: string;
  details?: Record<string, unknown>;
}

export class FetchError extends Error {
  constructor(
    public readonly status: number,
    public readonly details: ApiErrorBody
  ) {
    super(details.message);
  }
}

export function isFetchError(e: unknown): e is FetchError {
  return e instanceof FetchError;
}

async function getRequestHeaders() {
  return {
    "Content-Type": "application/json",
  };
}

async function handleResponse<TRes>(response: Response) {
  if (response.status >= 400) {
    try {
      const responseBody = (await response.json()) as ApiErrorBody;
      console.error("api error", JSON.stringify({ responseBody }));
      throw new FetchError(response.status, responseBody);
    } catch (e) {
      const responseText = await response.text();
      console.error("non-json response", { responseText });
      throw new Error(`http error ${response.status}: ${responseText}`);
    }
  } else {
    return (await response.json()) as TRes;
  }
}

export async function basePost<TReq, TRes>(
  path: string,
  data: TReq
): Promise<TRes> {
  const url = `${config.apiServer}${path}`;
  console.log("post", url, JSON.stringify(data));
  const response = await fetch(url, {
    method: "POST",
    headers: await getRequestHeaders(),
    body: JSON.stringify(data),
  });
  return await handleResponse<TRes>(response);
}

export async function baseGet<TRes, TParams = unknown>(
  path: string,
  params?: TParams
): Promise<TRes> {
  const queryString = params ? `?${new URLSearchParams(params)}` : "";
  const url = `${config.apiServer}${path}${queryString}`;
  console.log("get", url);
  const response = await fetch(url, {
    method: "GET",
    headers: await getRequestHeaders(),
  });
  return await handleResponse<TRes>(response);
}

export function useBaseGet<TRes, TParams = unknown>(
  path: string | null | undefined,
  params?: TParams
) {
  // TODO : there is a bug which is that if the params don't change, the data won't be refetched
  return useSWR(path, (p) => baseGet<TRes, TParams>(p, params));
}
