/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

/**
 * Choice is a possible choice to make in response to an Event
 * This choice will have an impact on the world and how the story progresses
 * It could lead to the world ending sooner, or later
 */
export interface Choice {
  /**
   * The choice to make in response to the event
   */
  choice: string;
  /**
   * The outcome of the choice made in response to the event
   */
  consequence: string;
}
/**
 * Event is a possible World Ending event, with a list of possible outcomes
 * country and city fields should represent a real location
 */
export interface Event {
  /**
   * The country where the apocalyptic event is happening
   */
  country: string;
  /**
   * The city where the predicted pivotal event is happening
   */
  city: string;
  /**
   * A two to three sentence description of the event and its outcome
   */
  description: string;
  /**
   * Three possible choices to take in reaction to this event, which will dictate the next event in the world
   */
  possible_choices: Choice[];
}
export interface GMRequest {
  query: string;
}
export interface GMResponse {
  game_master: GameMaster;
}
/**
 * GameMaster is the main class for the game master, who controls the game
 * mainly, he controls what is done with the input from the player
 */
export interface GameMaster {
  /**
   * The chain of thought that led to the decision
   */
  cot?: string;
  /**
   * The action that the player can take
   */
  action: Move | Build | Research;
}
/**
 * Move is a possible action that the player can take
 */
export interface Move {
  /**
   * The name of the destination city
   */
  destination: string;
  [k: string]: unknown;
}
/**
 * Build is a possible action that the player can take
 */
export interface Build {
  /**
   * The description of the building including the type and name
   */
  building: string;
  [k: string]: unknown;
}
/**
 * Research is a possible action that the player can take
 */
export interface Research {
  /**
   * The description of the research including the field and name
   */
  research: string;
  [k: string]: unknown;
}
/**
 * A plan of action
 */
export interface GamePlan {
  /**
   * A list of hints to help the player, these hints would make good queries for figuring out the game plan's goal
   */
  query_hints: string[];
  /**
   * The goal of the game plan, the thing the player needs to find to progress the game
   */
  goal: string;
}
export interface Illustration {
  prompt: string;
  negative_prompt: string;
  aspect_ratio: string;
  image_path: string;
  progress?: "none" | "inprogress" | "complete" | "failed";
}
/**
 * A location with a latitude and longitude.
 * Parent and children are used to create a tree structure.
 * The destroyed flag is used to mark a location as destroyed.
 */
export interface Location {
  /**
   * Latitude of the location
   */
  latitude: number;
  /**
   * Longitude of the location
   */
  longitude: number;
  /**
   * The parent location
   */
  parent?: Location | null;
  /**
   * The children locations
   */
  children?: Location[];
  /**
   * Whether the location is destroyed
   */
  destroyed?: boolean;
}
export interface NewIllustrationRequest {
  prompt: string;
  negative_prompt: string;
  aspect_ratio: string;
}
export interface NewIllustrationResponse {
  id: string;
  result: Illustration;
}
export interface NewScenarioRequest {
  player_name: string;
  city: string;
  scenario: string;
}
export interface NewScenarioResponse {
  slug: string;
  result: "success" | "failure";
}
/**
 * Outcome is the likely outcome from an Event, taking into account
 * recent developments in obscure wars, as we believe their impact
 * is more nuanced and far reaching than the government realizes.
 */
export interface Outcome {
  /**
   * An unlikely but scary outcome description, one we didn't see coming
   */
  description: string;
}
export interface Player {}
/**
 * A response to a question about the world ending event. There is a correct question to ask that will reveal hidden information in the game.
 */
export interface QuestionResponse {
  /**
   * Indicate if this was the correct question to ask
   */
  correct_question: boolean;
  /**
   * The response to the question
   */
  response: string;
}
export interface Scenario {
  slug: string;
  world: World;
  player: Player;
  last_event: Event | null;
  last_world_ender: WorldEnder | null;
  events?: Event[];
  world_enders?: WorldEnder[];
  question_response: QuestionResponse | null;
  final_population: number | null;
  Outcome: Outcome | null;
}
/**
 * World for the WorldEnder.ai game.
 * The world is a tree of locations.
 * The population ticks down according to the log_multiplier, which is set by
 * the events in the game.
 */
export interface World {
  /**
   * The current location of the player
   */
  current_location?: Location;
  /**
   * The population of the world
   */
  population?: number;
  /**
   * The number of days that have passed in the game
   */
  day?: number;
  /**
   * The log multiplier for the population decrease
   */
  log_multiplier?: number;
  epoch?: "Apocalyptic" | "Post-Apocalyptic" | "Post-Post-Apocalyptic";
}
/**
 * An apocalyptic event that the human race, and likely the world, cannot come back from.
 * This will likely be a nuclear event. The consequences will likely be long term fallout.
 * The class should tell the story of how we got here and why these things happened.
 */
export interface WorldEnder {
  /**
   * What kind of world ending event was this? (astrological, biological, war, etc.)
   */
  kind: string;
  /**
   * A detailed description of what happened, including the Events and Outcomes involved
   */
  description: string;
  /**
   * The total estimated cost of human life as a readable number example: 1bil
   */
  death_toll: string;
  /**
   * The percentage chance that any humans will survive the world ending event
   */
  survival_rate: number;
}
