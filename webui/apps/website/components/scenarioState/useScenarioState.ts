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
  const [isChoosing, setIsChoosing] = React.useState(false);
  const dataHook = useBaseGet<Scenario>(getScenarioUri(slug));
  //   console.log(JSON.stringify({ dataHook }));
  const [betterIdea, setBetterIdea] = React.useState("");
  const chooseIdea = React.useCallback(
    async (idea: string) => {
      try {
        setIsChoosing(true);
        const response = await basePost<Choice, Scenario>(
          postScenarioChooseUri(slug),
          {
            choice: idea,
            consequence: "",
          }
        );
        console.log(JSON.stringify({ response }));
        setBetterIdea("");
        dataHook.mutate(response);
      } catch (e) {
        if (isFetchError(e)) {
          // TODO : toast!
        }
      } finally {
        setIsChoosing(false);
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
      isLoading: isChoosing || dataHook.isLoading,
      betterIdea,
      setBetterIdea,
      handleBetterIdea,
      handleAction,
    }),
    [
      dataHook.data,
      dataHook.isLoading,
      isChoosing,
      betterIdea,
      handleBetterIdea,
      handleAction,
    ]
  );
}
