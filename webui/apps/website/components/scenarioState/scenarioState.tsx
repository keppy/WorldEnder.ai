"use client";
/**
 * This code was generated by v0 by Vercel.
 * @see https://v0.dev/t/d1YOe5PDmPx
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */

/** Add fonts into your Next.js project:

import { Chivo } from 'next/font/google'

chivo({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
import Link from "next/link";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import { Button } from "@/components/ui/button";
import React from "react";
import { ArrowUpIcon, HomeIcon } from "@radix-ui/react-icons";
import { useScenarioState } from "./useScenarioState";
import { Overlay } from "../ui/overlay";

interface Props {
  slug: string;
}

const constructQuery = (evenDescription: string, choice: string) => {
  return `
    ${evenDescription},
    you observed these hardships on the world and decided to
    ${choice}. What happens next?`;
};

const DisplayScenarioState = (hook: ReturnType<typeof useScenarioState>) => {
  if (!hook.data) {
    return <p>No data</p>;
  }
  let display: string = "";
  if (hook.data?.last_world_ender?.description) {
    display = hook.data.last_world_ender.description;
  } else if (hook.data?.last_event?.description) {
    display = hook.data.last_event.description;
  }
  return display;
};

export const ScenarioState: React.FC<Props> = ({ slug }) => {
  const hook = useScenarioState(slug);
  console.log(JSON.stringify({ isLoading: hook.isLoading }));
  return (
    <div className="flex min-h-screen flex-col bg-gray-950 text-gray-50 relative">
      <div className="flex items-center justify-between p-4">
        <Link
          href="/"
          className="m-4 p-4 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors self-start"
          prefetch={false}
        >
          <HomeIcon className="w-6 h-6 text-gray-900 dark:text-gray-100" />
        </Link>
        <div className="flex flex-col ">
          <div className="text-xl space-y-4 min-w-[360px]">
            {`${hook.data?.world.day} days have passed.`}
          </div>
          <div className="text-xl space-y-4 min-w-[360px]">
            {`The world population is ${hook.data?.world.population?.toLocaleString()}.`}
          </div>
        </div>
      </div>
      <div className="container mx-auto px-4 py-12 md:px-6 md:py-16 lg:py-20 flex flex-wrap items-center">
        <div className="space-y-8 flex-1 mr-8">
          <div className="text-xl space-y-4 flex-1 min-w-[360px] mb-8">
            {DisplayScenarioState(hook)}
          </div>
        </div>
        <img
          alt="Image"
          className="min-w-[360px] rounded-lg object-cover self-start"
          height={360}
          src="/we_hero.png"
          style={{
            aspectRatio: "360/360",
            objectFit: "cover",
          }}
          width={360}
        />
      </div>
      <section className="bg-gray-900 py-12 md:py-16 lg:py-20">
        <div className="container mx-auto px-4 md:px-6">
          <div className="space-y-8">
            <h2 className="text-3xl font-bold tracking-tighter md:text-4xl lg:text-5xl">
              Take Action:
            </h2>
            <div className="grid gap-6 md:grid-cols-3">
              <Link
                className="flex h-full flex-col rounded-lg border-[3px] border-white bg-gray-950 p-6 transition-all hover:bg-gray-800"
                href="#"
                onClick={() =>
                  hook.handleAction(
                    constructQuery(
                      hook.data?.last_event?.description ?? "",
                      hook.data?.last_event?.possible_choices[0].choice ?? ""
                    )
                  )
                }
              >
                <h3 className="text-2xl font-bold">
                  {hook.data?.last_event?.possible_choices[0].choice}
                </h3>
              </Link>
              <Link
                className="flex h-full flex-col rounded-lg border-[3px] border-white bg-gray-950 p-6 transition-all hover:bg-gray-800"
                href="#"
                onClick={() =>
                  hook.handleAction(
                    constructQuery(
                      hook.data?.last_event?.description ?? "",
                      hook.data?.last_event?.possible_choices[1].choice ?? ""
                    )
                  )
                }
              >
                <h3 className="text-2xl font-bold">
                  {hook.data?.last_event?.possible_choices[1].choice}
                </h3>
              </Link>
              <Link
                className="flex h-full flex-col rounded-lg border-[3px] border-white bg-gray-950 p-6 transition-all hover:bg-gray-800"
                href="#"
                onClick={() =>
                  hook.handleAction(
                    constructQuery(
                      hook.data?.last_event?.description ?? "",
                      hook.data?.last_event?.possible_choices[2].choice ?? ""
                    )
                  )
                }
              >
                <h3 className="text-2xl font-bold">
                  {hook.data?.last_event?.possible_choices[2].choice}
                </h3>
              </Link>
            </div>
          </div>
        </div>
      </section>
      <section className="container mx-auto px-4 py-12 md:px-6 md:py-16 lg:py-20">
        <div className="grid gap-4">
          <Label htmlFor="message" className="text-3xl">
            or...
          </Label>
          <Textarea
            id="message"
            placeholder="you have a better idea."
            value={hook.betterIdea}
            onChange={(ev) => hook.setBetterIdea(ev.target.value)}
          />
          <Button className="w-full" onClick={hook.handleBetterIdea}>
            Submit
          </Button>
        </div>
      </section>
      <div className="flex items-center justify-between p-4">
        <Link
          href="#"
          className="m-4 p-4 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors self-start"
          prefetch={false}
          onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
        >
          <ArrowUpIcon className="w-6 h-6 text-gray-900 dark:text-gray-100" />
        </Link>
        <div className="flex flex-col ">
          <div className="text-xl space-y-4 min-w-[360px]">
            {`${hook.data?.world.day} days have passed.`}
          </div>
          <div className="text-xl space-y-4 min-w-[360px]">
            {`The world population is ${hook.data?.world.population}.`}
          </div>
        </div>
      </div>
      {hook.isLoading && (
        <Overlay>
          <div className="space-y-8">
            <h2 className="text-3xl font-bold tracking-tighter md:text-4xl lg:text-5xl">
              You have decided to take action!
            </h2>
          </div>
        </Overlay>
      )}
    </div>
  );
};
