import { ScenarioState } from "@/components/scenarioState/scenarioState";

export default function ScenarioId({ params }: { params: { id: string } }) {
  return <ScenarioState slug={params.id} />;
}
