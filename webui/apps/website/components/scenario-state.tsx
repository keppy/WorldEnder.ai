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
import { HomeIcon } from "@radix-ui/react-icons";

export function ScenarioState() {
  const [paragraphText, setParagraphText] = React.useState(
    "A massive wildfire has erupted in the Amazon rainforest near Manaus, Brazil. The fire is spreading rapidly due to dry conditions and strong winds, threatening biodiversity and local communities. The smoke from the fire could potentially affect air quality across South America."
  );
  return (
    <div className="flex min-h-screen flex-col bg-gray-950 text-gray-50">
      <Link
        href="/"
        className="m-4 p-4 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors self-start"
        prefetch={false}
      >
        <HomeIcon className="w-6 h-6 text-gray-900 dark:text-gray-100" />
      </Link>
      <div className="container mx-auto px-4 py-12 md:px-6 md:py-16 lg:py-20 flex flex-wrap items-center">
        <div className="space-y-8 flex-1 mr-8">
          <div className="text-xl space-y-4 flex-1">{paragraphText}</div>
        </div>
        <img
          alt="Image"
          className="min-w-[360px] rounded-lg object-cover"
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
              >
                <h3 className="text-2xl font-bold">
                  Increase international firefighting efforts
                </h3>
              </Link>
              <Link
                className="flex h-full flex-col rounded-lg border-[3px] border-white bg-gray-950 p-6 transition-all hover:bg-gray-800"
                href="#"
              >
                <h3 className="text-2xl font-bold">Ignore the fire</h3>
              </Link>
              <Link
                className="flex h-full flex-col rounded-lg border-[3px] border-white bg-gray-950 p-6 transition-all hover:bg-gray-800"
                href="#"
              >
                <h3 className="text-2xl font-bold">
                  Focus on local containment
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
          <Textarea id="message" placeholder="you have a better idea." />
          <Button className="w-full" type="submit">
            Submit
          </Button>
        </div>
      </section>
    </div>
  );
}
