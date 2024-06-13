import {
  FetchError,
  basePost,
  isFetchError,
  postScenarioNewUri,
} from "@/lib/apiServer";
import { NewScenarioRequest, NewScenarioResponse } from "@/lib/dtos";
import { useRouter } from "next/navigation";
import React from "react";

export function useNewScenario() {
  const [showForm, setShowForm] = React.useState(true);
  const router = useRouter();
  const handleAccept = React.useCallback(() => {
    setShowForm(false);
  }, []);
  const [name, setName] = React.useState("");
  const [city, setCity] = React.useState("");
  const [worldEndingEvent, setWorldEndingEvent] = React.useState("");

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
      setName,
      city,
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
      showForm,
      worldEndingEvent,
    ]
  );
}
