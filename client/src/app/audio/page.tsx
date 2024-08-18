"use client";

import { useState, ChangeEvent, FormEvent } from "react";
import { Button } from "@/components/ui/button";
// import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
// import { faMicrophone, faStop } from "@fortawesome/free-solid-svg-icons";
import Header from "@/components/ui/header";
import toast, { Toaster } from "react-hot-toast";

export default function AudioInput() {
  const [audioFile, setAudioFile] = useState<File | null>(null);
  // const [isRecording, setIsRecording] = useState<boolean>(false);
  const [audioURL, setAudioURL] = useState<string | null>(null);
  // const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  // const audioChunksRef = useRef<Blob[]>([]);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!audioFile && !audioURL) {
      toast.error("Please upload an audio file or record one.");
      return;
    }

    const formData = new FormData();
    if (audioFile) {
      formData.append("audio", audioFile);
    } else if (audioURL) {
      const response = await fetch(audioURL);
      const blob = await response.blob();
      formData.append("audio", blob, "recording.wav");
    }

    const toastId = toast.loading("Analyzing audio...");
    try {
      const response = await fetch(
        `${process.env.NEXT_PUBLIC_API_URL}/complaint/analyze_audio`,
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await response.json();

      if (data.success) {
        toast.success(data.message, { id: toastId });
      } else {
        toast.error(data.error || "An unknown error occurred.", {
          id: toastId,
        });
      }
    } catch (error) {
      console.error("Error submitting data:", error);
      toast.error("Error submitting data.", { id: toastId });
    }
    setAudioFile(null);
    setAudioURL(null);
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setAudioFile(e.target.files[0]);
      setAudioURL(null);
    }
  };

  // const startRecording = () => {
  //   navigator.mediaDevices
  //     .getUserMedia({ audio: true })
  //     .then((stream) => {
  //       const mediaRecorder = new MediaRecorder(stream);
  //       mediaRecorderRef.current = mediaRecorder;
  //       mediaRecorder.ondataavailable = (event) => {
  //         audioChunksRef.current.push(event.data);
  //       };
  //       mediaRecorder.onstop = () => {
  //         const audioBlob = new Blob(audioChunksRef.current, {
  //           type: "audio/wav",
  //         });
  //         const url = URL.createObjectURL(audioBlob);
  //         setAudioURL(url);
  //         setAudioFile(null);
  //         audioChunksRef.current = [];
  //       };
  //       mediaRecorder.start();
  //       setIsRecording(true);
  //     })
  //     .catch((error) => console.error("Error accessing media devices.", error));
  // };

  // const stopRecording = () => {
  //   if (mediaRecorderRef.current) {
  //     mediaRecorderRef.current.stop();
  //     setIsRecording(false);
  //   }
  // };

  return (
    <>
      <Toaster />
      <Header />
      <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 px-5">
        <div className="text-center">
          <h1 className="text-4xl md:text-5xl font-bold mb-6 text-[#0e312d]">
            Upload or Record an Audio File
          </h1>
          <h2 className="text-base md:text-lg text-gray-600 mb-8">
            Please upload your audio file below or record one directly.
          </h2>
          <form
            onSubmit={handleSubmit}
            className="space-y-4 max-w-md md:max-w-lg mx-auto"
          >
            <label className="w-full flex items-center justify-center bg-white py-4 px-6 border border-gray-300 rounded-md shadow-sm cursor-pointer hover:bg-gray-50">
              <span className="text-gray-700">Choose an audio file</span>
              <input
                type="file"
                accept="audio/*"
                onChange={handleFileChange}
                className="sr-only"
              />
            </label>
            {audioFile && <p className="text-gray-700">{audioFile.name}</p>}
            {/* <div className="text-sm text-gray-500">
              Or record your own audio
            </div>
            <div className="flex items-center justify-center pb-2">
              <Button
                type="button"
                onClick={isRecording ? stopRecording : startRecording}
                className={`w-12 h-12 rounded-full flex items-center justify-center text-white ${
                  isRecording
                    ? "bg-red-400 hover:bg-red-500"
                    : "bg-black hover:bg-slate-800"
                }`}
              >
                <FontAwesomeIcon
                  icon={isRecording ? faStop : faMicrophone}
                  className="text-2xl"
                />
              </Button>
            </div>
            {audioURL && (
              <div className="mt-4">
                <audio controls src={audioURL} />
                <p className="text-gray-700 mt-2">Recorded Audio</p>
              </div>
            )} */}
            <Button
              type="submit"
              className="shadow-sm shadow-black w-full text-black bg-[#E9E3A6] hover:bg-[#ded890]"
            >
              Submit
            </Button>
          </form>
        </div>
      </div>
    </>
  );
}
