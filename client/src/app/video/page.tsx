'use client';

import { useState, ChangeEvent, FormEvent } from 'react';
import { Button } from '@/components/ui/button';

export default function VideoInput() {
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [videoURL, setVideoURL] = useState<string | undefined>(undefined);
  const [status, setStatus] = useState<string>('');

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!videoFile) {
      setStatus('Please upload a video file.');
      return;
    }

    const formData = new FormData();
    formData.append('video', videoFile);

    try {
      const response = await fetch('url-todo', {
        method: 'POST',
        body: formData,
      });

      const data = await response.json();
      setStatus(data.message);
    } catch (error) {
      console.error('Error submitting data:', error);
      setStatus('Error submitting data.');
    }
  };

  const handleFileChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      const file = e.target.files[0];
      setVideoFile(file);
      setVideoURL(URL.createObjectURL(file));
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 px-4 py-8">
      <div className="text-center">
        <h1 className="text-4xl md:text-5xl font-bold mb-6 text-[#0e312d]">Upload a Video File</h1>
        <h2 className="text-base md:text-lg text-gray-600 mb-8">Please upload your video file below.</h2>
        <form onSubmit={handleSubmit} className="space-y-4 max-w-md md:max-w-lg mx-auto">
          <label className="w-full flex flex-col items-center justify-center bg-white py-4 px-6 border border-gray-300 rounded-md shadow-sm cursor-pointer hover:bg-gray-50">
            <span className="text-gray-700">Choose a video file</span>
            <input type="file" accept="video/*" onChange={handleFileChange} className="sr-only" />
          </label>
          {videoFile && (
            <div className="mt-4">
              <video controls src={videoURL} className="w-full h-auto max-w-lg rounded-md shadow-md" />
              <p className="text-gray-700 mt-2">{videoFile.name}</p>
            </div>
          )}
          <Button type="submit" className="shadow-sm shadow-black w-full text-black bg-[#E9E3A6] hover:bg-[#ded890]">Submit</Button>
        </form>
        {status && <p className="mt-4 text-sm text-red-400">{status}</p>}
      </div>
    </div>
  );
}
