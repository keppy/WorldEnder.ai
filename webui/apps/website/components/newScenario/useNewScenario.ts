import {
  FetchError,
  baseGet,
  basePost,
  getFullUri,
  getIllustrationImageUri,
  getIllustrationUri,
  isFetchError,
  postIllustrationNewUri,
  postScenarioNewUri,
} from "@/lib/apiServer";
import {
  Illustration,
  NewIllustrationRequest,
  NewIllustrationResponse,
  NewScenarioRequest,
  NewScenarioResponse,
} from "@/lib/dtos";
import { useRouter } from "next/navigation";
import React from "react";
import useSWR from "swr";

export function useNewScenario() {
  const [showForm, setShowForm] = React.useState(true);
  const router = useRouter();
  const [name, setName] = React.useState("");
  const [city, setCity] = React.useState("");
  const [showOverlay, setShowOverlay] = React.useState(false);
  const [heroIllustrationId, setHeroIllustrationId] = React.useState<string>();
  const [newHeroUri, setNewHeroUri] = React.useState<string>();
  const [worldEndingEvent, setWorldEndingEvent] = React.useState("");
  const handleAccept = React.useCallback(async () => {
    // TODO wait on response
    console.log("Accept");
    setShowOverlay(true);
    try {
      const req = {
        prompt: `comic book: ${name} wakes up in ${city}:foreboding`,
        negative_prompt: "no text; full clothing;",
        aspect_ratio: "9:16",
      };
      const response = await basePost<
        NewIllustrationRequest,
        NewIllustrationResponse
      >(postIllustrationNewUri(), req);
      console.log("got response to new illustration", response.id);
      let status = response.result.progress;
      let r2: Illustration;
      while (!["complete", "failed"].includes(status ?? "")) {
        r2 = await baseGet<Illustration>(getIllustrationUri(response.id));
        console.log("retry", JSON.stringify(r2));
        status = r2.progress;
        await new Promise((resolve) => setTimeout(resolve, 1000));
      }
      console.log("final status", status);
      setNewHeroUri(getFullUri(getIllustrationImageUri(response.id)));
    } catch (e) {
      console.error(e);
    } finally {
      console.log;
      setShowOverlay(false);
      setShowForm(false);
    }
  }, [city, name]);

  const acceptEnabled = name.length > 0 && city.length > 0;
  const continueEnabled = worldEndingEvent.length > 0;

  const handleContinue = React.useCallback(async () => {
    console.log("Continue");
    try {
      const response = await basePost<NewScenarioRequest, NewScenarioResponse>(
        postScenarioNewUri(),
        {
          player_name: name,
          city,
          scenario: worldEndingEvent,
        }
      );
      if (response.result === "success") {
        router.push(`/scenario/${response.slug}`);
      }
    } catch (e) {
      if (isFetchError(e)) {
        // TODO : toast!
      }
    }
  }, [city, name, router, worldEndingEvent]);

  return React.useMemo(
    () => ({
      showForm,
      handleAccept,
      handleContinue,
      name,
      showOverlay,
      setName,
      city,
      newHeroUri,
      setCity,
      acceptEnabled,
      continueEnabled,
      worldEndingEvent,
      setWorldEndingEvent,
    }),
    [
      acceptEnabled,
      city,
      continueEnabled,
      handleAccept,
      handleContinue,
      name,
      newHeroUri,
      showForm,
      showOverlay,
      worldEndingEvent,
    ]
  );
}
