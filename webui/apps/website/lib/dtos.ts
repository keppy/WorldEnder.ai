/* tslint:disable */
/* eslint-disable */
/**
/* This file was automatically generated from pydantic models by running pydantic2ts.
/* Do not modify it by hand - just update the pydantic models and then re-run the script
*/

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
  [k: string]: unknown;
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
export interface Scenario {
  slug: string;
  world: World;
  player: Player;
  last_event: Event | null;
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
  [k: string]: unknown;
}
