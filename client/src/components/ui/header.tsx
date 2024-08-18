'use client';

import { useState } from 'react';
import { Button } from './button';
import Link from 'next/link';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faBars, faTimes } from '@fortawesome/free-solid-svg-icons';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="py-6 w-full bg-white shadow-md">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-3xl font-bold">
          <Link href="/">SortItOut</Link>
        </h1>
        <nav className="hidden md:flex space-x-5 items-center">
          <Link href="/" className="hover:underline">Text</Link>
          <Link href="/audio" className="hover:underline">Audio</Link>
          <Link href="/video" className="hover:underline">Video</Link>
          <Link href="/image" className="hover:underline pr-5">Image</Link>
          <Button>Log out</Button>
        </nav>
        <button
          className="md:hidden text-2xl"
          onClick={toggleMenu}
          aria-label={isMenuOpen ? 'Close menu' : 'Open menu'}
        >
          <FontAwesomeIcon icon={isMenuOpen ? faTimes : faBars} />
        </button>
        <nav className={`md:hidden fixed inset-0 w-full h-full bg-white shadow-lg transition-transform transform ${isMenuOpen ? '-translate-y-0' : '-translate-y-full'} z-50`}>
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
              <Link href="/" onClick={toggleMenu} className="text-xl hover:underline">Text</Link>
              <Link href="/audio" onClick={toggleMenu} className="text-xl hover:underline">Audio</Link>
              <Link href="/video" onClick={toggleMenu} className="text-xl hover:underline">Video</Link>
              <Link href="/image" onClick={toggleMenu} className="text-xl hover:underline pb-8">Image</Link>
              <Button onClick={toggleMenu} className="max-w-80 w-full">Log out</Button>
            </div>
          </div>
        </nav>
      </div>
    </header>
  );
};

export default Header;
