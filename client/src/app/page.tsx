"use client";

import Image from "next/image";
import { Button } from "@/components/ui/button";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import Link from "next/link";

export default function LandingPage() {
  return (
    <div className="bg-gray-100 text-gray-900">
      {/* Hero */}
      <section className="relative h-[500px] text-white flex items-center justify-center">
        <div className="absolute inset-0 z-0">
          <Image
            src="/imageLanding.jpg"
            alt="Hero Background"
            fill
            className="object-cover"
            quality={100}
          />
        </div>
        <div className="relative z-10 container mx-auto px-6">
          <div className="text-center">
            <h1 className="text-5xl font-extrabold mb-4">
              Transform Your Complaints
            </h1>
            <p className="text-lg mb-8">
              Effortlessly categorize and analyze complaints with our advanced
              AI-powered tool.
            </p>
            <Button className="bg-yellow-500 hover:bg-yellow-600 text-black py-3 px-6 rounded-lg">
              <Link href="/login">Get Started</Link>
            </Button>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-12">
            What We Offer
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            <div className="relative bg-gray-200 rounded-lg overflow-hidden shadow-lg transition-transform transform hover:scale-105 h-96">
              <Image
                src="/fastFeature.jpg"
                alt="Fast Analysis"
                fill
                className="w-full h-full object-cover"
              />
              <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center opacity-0 transition-opacity hover:opacity-100">
                <div className="text-center text-white p-6">
                  <h3 className="text-2xl font-semibold mb-4">Fast Analysis</h3>
                  <p className="text-lg">
                    Get our analysis responses in a matter of seconds.
                  </p>
                </div>
              </div>
            </div>

            <div className="relative bg-gray-200 rounded-lg overflow-hidden shadow-lg transition-transform transform hover:scale-105 h-96">
              <Image
                src="/aiFeature.jpg"
                alt="AI-Powered Insights"
                fill
                className="w-full h-full object-cover"
              />
              <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center opacity-0 transition-opacity hover:opacity-100">
                <div className="text-center text-white p-6">
                  <h3 className="text-2xl font-semibold mb-4">
                    AI-Powered Insights
                  </h3>
                  <p className="text-lg">
                    Get detailed analysis and insights with advanced AI
                    algorithms.
                  </p>
                </div>
              </div>
            </div>

            <div className="relative bg-gray-200 rounded-lg overflow-hidden shadow-lg transition-transform transform hover:scale-105 h-96">
              <Image
                src="/uiFeature.jpg"
                alt="User-Friendly Interface"
                fill
                className="w-full h-full object-cover"
              />
              <div className="absolute inset-0 bg-black bg-opacity-50 flex items-center justify-center opacity-0 transition-opacity hover:opacity-100">
                <div className="text-center text-white p-6">
                  <h3 className="text-2xl font-semibold mb-4">
                    User-Friendly Interface
                  </h3>
                  <p className="text-lg">
                    Enjoy a clean and intuitive interface that&apos;s easy to
                    navigate.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Key Benefits Section */}
      <section className="py-16 bg-gray-100">
        <div className="container mx-auto px-6 text-center">
          <h2 className="text-4xl font-bold mb-8">
            Efficiency and Speed in Every Decision
          </h2>
          <p className="text-lg mb-12">
            Discover how our solution benefits different types of users.
          </p>
          <div className="flex flex-wrap justify-center gap-12">
            <div className="bg-white p-8 rounded-lg shadow-lg max-w-md flex flex-col items-center">
              <div className="w-16 h-16 mb-4 flex items-center justify-center bg-yellow-500 rounded-full">
                <svg
                  className="w-10 h-10 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M3 10h18M3 6h18M3 14h18m-8 4h8M5 18h4m4-12H5m0 4h8m-4-4v8m4-4v4"
                  />
                </svg>
              </div>
              <h3 className="text-2xl font-semibold mb-4">For Businesses</h3>
              <p className="text-lg mb-4">
                Boost operational efficiency by analyzing user complaints to
                streamline processes and improve satisfaction.
              </p>
            </div>

            <div className="bg-white p-8 rounded-lg shadow-lg max-w-md flex flex-col items-center">
              <div className="w-16 h-16 mb-4 flex items-center justify-center bg-yellow-500 rounded-full">
                <svg
                  className="w-10 h-10 text-white"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth="2"
                    d="M12 5v7l5 2.5m-5-2.5l-5 2.5V5m0 0h10m-10 0L12 3m0 0l10 5m-10-5v7"
                  />
                </svg>
              </div>
              <h3 className="text-2xl font-semibold mb-4">For Schools</h3>
              <p className="text-lg mb-4">
                Enhance student feedback analysis by examining patterns and
                trends in similar complaints to foster a better learning
                environment.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Call-to-Action Section */}
      <section className="py-16 bg-yellow-500 text-white text-center">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold mb-4">Ready to Dive In?</h2>
          <p className="text-lg mb-8">
            Start analyzing complaints today with our powerful AI-driven
            solutions.
          </p>
          <Button className="bg-black hover:bg-gray-800 text-white py-3 px-6 rounded-lg">
            <Link href="/login">Get Started</Link>
          </Button>
        </div>
      </section>

      {/* Accordion Section */}
      <section className="py-16 bg-white">
        <div className="container mx-auto px-8 flex flex-col items-center">
          <h2 className="text-4xl font-bold text-center mb-12">FAQs</h2>
          <Accordion type="single" collapsible className="w-full max-w-xl">
            <AccordionItem value="item-1">
              <AccordionTrigger>Do I need an account?</AccordionTrigger>
              <AccordionContent>
                Yes. Complaints are sent by a user.
              </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-2">
              <AccordionTrigger>
                In what form can I send a complaint?
              </AccordionTrigger>
              <AccordionContent>
                You can send via text, audio, image, and video.
              </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-3">
              <AccordionTrigger>How does it work?</AccordionTrigger>
              <AccordionContent>
                Your input is analyzed by our AI and also compared for similar
                ones.
              </AccordionContent>
            </AccordionItem>
            <AccordionItem value="item-4">
              <AccordionTrigger>Can I make a google account?</AccordionTrigger>
              <AccordionContent>
                Our platform lets users sign in or log in with google.
              </AccordionContent>
            </AccordionItem>
          </Accordion>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-800 text-white py-8">
        <div className="container mx-auto px-6 text-center">
          <p className="mb-4">
            &copy; {new Date().getFullYear()} SortItOut. All rights reserved.
          </p>
        </div>
      </footer>
    </div>
    </>
  );
}