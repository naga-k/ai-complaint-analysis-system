"use client";

import { useState, ChangeEvent, FormEvent } from "react";
import { Button } from "@/components/ui/button";
import { Textarea } from "@/components/ui/textarea";
import Header from "@/components/ui/header";

export default function TextPage() {
  const [input, setInput] = useState<string>("");
  const [status, setStatus] = useState<string>("");

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/complaint/analyze`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ input }),
        }
      );

      const data = await response.json();
      setStatus(data.message);
    } catch (error) {
      console.error("Error submitting data:", error);
      setStatus("Error submitting data.");
    }
    setInput("");
  };

  const handleChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    setInput(e.target.value);
  };

  return (
    <>
      <Header />
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 px-4 py-8">
        <div className="text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6 text-[#0e312d]">
            Send your text complaint
          </h1>
          <h2 className="text-base md:text-lg text-gray-600 mb-8">
            Please enter your text below and click submit.
          </h2>
          <form
            onSubmit={handleSubmit}
            className="space-y-4 max-w-md md:max-w-lg mx-auto"
          >
            <Textarea
              value={input}
              onChange={handleChange}
              placeholder="Enter your text here..."
              rows={6}
              className="w-full"
            />
            <Button
              type="submit"
              className="shadow-sm shadow-black w-full text-black bg-[#E9E3A6] hover:bg-[#ded890]"
            >
              Submit
            </Button>
          </form>
          {status && <p className="mt-4 text-sm text-gray-500">{status}</p>}
        </div>
      </div>
    </>
  );
}
