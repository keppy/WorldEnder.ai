import {
  basePost,
  getScenarioUri,
  isFetchError,
  postScenarioChooseUri,
  useBaseGet,
} from "@/lib/apiServer";
import { Choice, Scenario } from "@/lib/dtos";
import React from "react";

export function useScenarioState(slug: string) {
  const dataHook = useBaseGet<Scenario>(getScenarioUri(slug));
  //   console.log(JSON.stringify({ dataHook }));
  const [betterIdea, setBetterIdea] = React.useState("");
  const chooseIdea = React.useCallback(
    async (idea: string) => {
      try {
        const response = await basePost<Choice, Scenario>(
          postScenarioChooseUri(slug),
          {
            choice: idea,
            predefined_index: 0,
          }
        );
        console.log(JSON.stringify({ response }));
        setBetterIdea("");
        dataHook.mutate(response);
      } catch (e) {
        if (isFetchError(e)) {
          // TODO : toast!
        }
      }
    },
    [dataHook, slug]
  );
  const handleBetterIdea = React.useCallback(async () => {
    chooseIdea(betterIdea);
  }, [betterIdea, chooseIdea]);
  const handleAction = React.useCallback(
    async (action: string) => {
      chooseIdea(action);
    },
    [chooseIdea]
  );
  return React.useMemo(
    () => ({
      data: dataHook.data,
      betterIdea,
      setBetterIdea,
      handleBetterIdea,
      handleAction,
    }),
    [betterIdea, dataHook.data, handleAction, handleBetterIdea]
  );
}
