/**
* This code was generated by v0 by Vercel.
* @see https://v0.dev/t/MF5n7WpklJ3
* Documentation: https://v0.dev/docs#integrating-generated-code-into-your-nextjs-app
*/

/** Add fonts into your Next.js project:

import { Libre_Franklin } from 'next/font/google'
import { Chivo } from 'next/font/google'

libre_franklin({
  subsets: ['latin'],
  display: 'swap',
})

chivo({
  subsets: ['latin'],
  display: 'swap',
})

To read more about using these font, please visit the Next.js documentation:
- App Directory: https://nextjs.org/docs/app/building-your-application/optimizing/fonts
- Pages Directory: https://nextjs.org/docs/pages/building-your-application/optimizing/fonts
**/
import { Textarea } from "@/components/ui/textarea"

export function ShareThoughts() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen px-4 py-8">
      <h2 className="text-2xl font-bold mb-4">Share Your Thoughts</h2>
      <div className="bg-white dark:bg-gray-900 rounded-lg shadow-md p-6 w-full max-w-md">
        <Textarea
          className="w-full h-40 resize-both rounded-md p-4 text-gray-900 dark:text-gray-100 focus:outline-none focus:ring-2 focus:ring-blue-500 dark:focus:ring-blue-400"
          placeholder="Type your message here..."
        />
      </div>
    </div>
  )
}