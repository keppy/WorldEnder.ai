/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

/**
 * Enumeration representing the types of queries that can be asked to a question answer system.
 */
export type QueryType = "SINGLE" | "MERGE_MULTIPLE_RESPONSES";

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
 * Event is a possilbe World Ending event, with a list of possible outcomes
 * country and city fields should represent a real location
 */
export interface Event {
  /**
   * The country where the apocolyptic event is happening
   */
  country: string;
  /**
   * The city where the predicted pivitol event is happening
   */
  city: string;
  /**
   * A two to three sentance description of the event and its outcome
   */
  description: string;
  /**
   * Three possible choices to take in reaction to this event, which will dictate the next event in the world
   */
  possible_choices: Choice[];
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
 * Container class representing a tree of questions to ask a question answer system.
 * and its dependencies. Make sure every question is in the tree, and every question is asked only once.
 */
export interface QueryPlan {
  /**
   * The original question we are asking
   */
  query_graph: Query[];
}
/**
 * Class representing a single question in a question answer subquery.
 * Can be either a single question or a multi question merge.
 */
export interface Query {
  /**
   * Unique id of the query
   */
  id: number;
  /**
   * Question we are asking using a question answer system, if we are asking multiple questions, this question is asked by also providing the answers to the sub questions
   */
  question: string;
  /**
   * List of sub questions that need to be answered before we can ask the question. Use a subquery when anything may be unknown, and we need to ask multiple questions to get the answer. Dependences must only be other queries.
   */
  dependancies?: number[];
  /**
   * Type of question we are asking, either a single question or a multi question merge when there are multiple questions
   */
  node_type?: QueryType & string;
  [k: string]: unknown;
}
export interface Scenario {
  slug: string;
  world: World;
  player: Player;
  last_event: Event | null;
  last_world_ender: WorldEnder | null;
  events?: Event[];
  world_enders?: WorldEnder[];
  query_plan: QueryPlan | null;
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
 * An apocolyptic event that the human race, and likely the world, cannot come back from.
 * This will likely be a nuclear event. The consiquences will likely be long term fallout.
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
  /**
   * Three choices you could take to try and combat the world ending event
   *
   * @minItems 3
   * @maxItems 3
   */
  choices: [string, string, string];
}
