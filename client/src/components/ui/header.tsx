"use client";

import { useEffect, useState } from "react";
import { Button } from "./button";
import Link from "next/link";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faBars, faTimes } from "@fortawesome/free-solid-svg-icons";
import { useParams } from "next/navigation";
import { useRouter } from "next/navigation";
import { createClient } from "@/utils/supabase/client";

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [userId, setUserId] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const router = useRouter();
  const params = useParams();
  const supabase = createClient();

  useEffect(() => {
    const checkUser = async () => {
      const {
        data: { user },
      } = await supabase.auth.getUser();
      if (user) {
        setUserId(user.id);
      } else {
        router.push("/login");
      }
      setIsLoading(false);
    };

    if (!!supabase) {
      checkUser();
    }
  }, [supabase, router]);

  useEffect(() => {
    const urlUserId = params.userId;
    if (userId && urlUserId && urlUserId !== userId) {
      router.push("/login");
    }
  }, [userId, params.userId, router]);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const handleLogout = async () => {
    await supabase.auth.signOut();
    router.push("/login");
  };

  if (isLoading) {
    return <div></div>;
  }

  return (
    <header className="py-6 w-full bg-white shadow-md fixed top-0 left-0 block">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-3xl font-bold">
          <Link href={`/dashboard/${userId}/text`}>SortItOut</Link>
        </h1>
        <nav className="hidden md:flex space-x-5 items-center">
          <Link href={`/dashboard/${userId}/text`} className="hover:underline">
            Text
          </Link>
          <Link href={`/dashboard/${userId}/audio`} className="hover:underline">
            Audio
          </Link>
          <Link href={`/dashboard/${userId}/video`} className="hover:underline">
            Video
          </Link>
          <Link
            href={`/dashboard/${userId}/image`}
            className="hover:underline pr-5"
          >
            Image
          </Link>
          <Button onClick={handleLogout}>Log out</Button>
        </nav>
        <button
          className="md:hidden text-2xl"
          onClick={toggleMenu}
          aria-label={isMenuOpen ? "Close menu" : "Open menu"}
        >
          <FontAwesomeIcon icon={isMenuOpen ? faTimes : faBars} />
        </button>
        <nav
          className={`md:hidden fixed inset-0 w-full h-full bg-white shadow-lg transition-transform transform ${
            isMenuOpen ? "-translate-y-0" : "-translate-y-full"
          } z-50`}
        >
          <div className="flex flex-col h-full">
            <div className="flex justify-end p-5">
              <button
                className="text-2xl"
                onClick={toggleMenu}
                aria-label="Close menu"
              >
                <FontAwesomeIcon icon={faTimes} />
              </button>
            </div>
            <div className="flex flex-col items-center justify-center flex-grow space-y-4">
              <Link
                href={`/dashboard/${userId}/text`}
                onClick={toggleMenu}
                className="text-xl hover:underline"
              >
                Text
              </Link>
              <Link
                href={`/dashboard/${userId}/audio`}
                onClick={toggleMenu}
                className="text-xl hover:underline"
              >
                Audio
              </Link>
              <Link
                href={`/dashboard/${userId}/video`}
                onClick={toggleMenu}
                className="text-xl hover:underline"
              >
                Video
              </Link>
              <Link
                href={`/dashboard/${userId}/image`}
                onClick={toggleMenu}
                className="text-xl hover:underline pb-8"
              >
                Image
              </Link>
              <Button
                onClick={() => {
                  handleLogout();
                  toggleMenu();
                }}
                className="max-w-80 w-full"
              >
                Log out
              </Button>
            </div>
          </div>
        </nav>
      </div>
    </header>
  );
};

export default Header;
