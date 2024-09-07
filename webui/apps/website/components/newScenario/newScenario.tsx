/**
 * v0 by Vercel.
 * @see https://v0.dev/t/KEEx1j9QvBH
 * Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
 */
"use client";

import { useState } from "react";
import { Label } from "@/components/ui/label";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import Link from "next/link";
import { HomeIcon } from "@radix-ui/react-icons";
import { useRouter } from "next/navigation";
import { useNewScenario } from "./useNewScenario";
import { Overlay } from "../ui/overlay";

export function NewScenario() {
  const hook = useNewScenario();
  return (
    <div className="flex min-h-[100dvh] flex-col black-900 text-gray-50 bg-gray-950">
      <Link
        href="/"
        className="m-16 p-4 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors self-start"
        prefetch={false}
      >
        <HomeIcon className="w-6 h-6 text-gray-900 dark:text-gray-100" />
      </Link>
      <main className="container mx-auto flex flex-1 flex-col items-center justify-center px-4 py-12 md:px-6 lg:py-24">
        {hook.showForm ? (
          <div className="mx-auto w-full max-w-md space-y-6">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
              Begin the Ending...
            </h1>
            <div className="grid gap-2">
              <Label htmlFor="name">Name</Label>
              <Input
                id="name"
                placeholder="Enter your name"
                value={hook.name}
                onChange={(ev) => hook.setName(ev.target.value)}
              />
            </div>
            <div className="grid gap-2">
              <Label htmlFor="city">Starting City</Label>
              <Input
                id="city"
                placeholder="Enter your starting city"
                value={hook.city}
                onChange={(ev) => hook.setCity(ev.target.value)}
              />
            </div>
            <Button
              onClick={hook.handleAccept}
              className="w-full"
              disabled={!hook.acceptEnabled}
            >
              Accept
            </Button>
            {hook.showOverlay && (
              <Overlay>
                <div className="space-y-8">
                  <h2 className="text-3xl font-bold tracking-tighter md:text-4xl lg:text-5xl">
                    It begins...
                  </h2>
                </div>
              </Overlay>
            )}
          </div>
        ) : (
          <div className="mx-auto w-full max-w-md space-y-6">
            <img
              src={hook.newHeroUri}
              width="800"
              height="450"
              alt="Hero"
              className="mx-auto aspect-[9/16] w-full rounded-xl object-cover"
            />
            <div className="space-y-4">
              <p>
                You wake up in your same old room and feel a sense of dread.
                Something is not quite right in the world and you can&apos;t put
                your finger on it. Describe the world ending event which you are
                having a premonition about:
              </p>
              <Textarea
                className="h-32 w-full resize-both"
                placeholder="Describe the world ending event..."
                value={hook.worldEndingEvent}
                onChange={(ev) => hook.setWorldEndingEvent(ev.target.value)}
              />
              <Button
                onClick={hook.handleContinue}
                className="w-full"
                disabled={!hook.continueEnabled}
              >
                Continue
              </Button>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
