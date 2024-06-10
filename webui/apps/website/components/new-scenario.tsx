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

export function NewScenario() {
  const [showForm, setShowForm] = useState(true);
  const router = useRouter();
  const handleAccept = () => {
    setShowForm(false);
  };
  const handleContinue = () => {
    console.log("Continue");
    router.push("/scenario/1");
  };
  return (
    <div className="flex min-h-[100dvh] flex-col black-900 text-gray-50">
      <Link
        href="/"
        className="m-16 p-4 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition-colors self-start"
        prefetch={false}
      >
        <HomeIcon className="w-6 h-6 text-gray-900 dark:text-gray-100" />
      </Link>
      <main className="container mx-auto flex flex-1 flex-col items-center justify-center px-4 py-12 md:px-6 lg:py-24">
        {showForm ? (
          <div className="mx-auto w-full max-w-md space-y-6">
            <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
              Begin the Ending...
            </h1>
            <form className="space-y-4">
              <div className="grid gap-2">
                <Label htmlFor="name">Name</Label>
                <Input id="name" placeholder="Enter your name" />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="city">Starting City</Label>
                <Input id="city" placeholder="Enter your starting city" />
              </div>
              <Button onClick={handleAccept} className="w-full">
                Accept
              </Button>
            </form>
          </div>
        ) : (
          <div className="mx-auto w-full max-w-md space-y-6">
            <img
              src="/placeholder.svg"
              width="800"
              height="450"
              alt="Hero"
              className="mx-auto aspect-[16/9] w-full rounded-xl object-cover"
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
              />
              <Button onClick={handleContinue} className="w-full">
                Continue
              </Button>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
