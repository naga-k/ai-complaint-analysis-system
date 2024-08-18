"use client";

// import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

// export const metadata: Metadata = {
//   title: "Ai Complaint Analysis System",
//   description: "We analyze complaints based on given input",
// };

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        <title>Ai Complaint Analysis System</title>
        <meta
          name="description"
          content="We analyze complaints based on given input"
        />
      </head>
      <body className={inter.className}>{children}</body>
    </html>
  );
}
