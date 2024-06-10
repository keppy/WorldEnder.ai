import type { Metadata } from "next";
import { Orbitron, Share_Tech_Mono } from "next/font/google";
import "./globals.css";

const orbitron = Orbitron({ subsets: ["latin"], display: "swap" });
const share_tech = Share_Tech_Mono({
  subsets: ["latin"],
  display: "swap",
  weight: "400",
});

export const metadata: Metadata = {
  title: "WorldEnder.ai",
  description: "Welcome to WorldEnder.ai",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={share_tech.className}>{children}</body>
    </html>
  );
}
