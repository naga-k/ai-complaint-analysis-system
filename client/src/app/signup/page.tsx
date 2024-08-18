"use client";

import { useState, FormEvent, useCallback } from "react";
import Image from "next/image";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import toast, { Toaster } from "react-hot-toast";
import { createClient } from "@/utils/supabase/client";

export default function Signup() {
  const [form, setForm] = useState({
    firstName: "",
    lastName: "",
    email: "",
    password: "",
    confirmPassword: "",
  });
  const [isLoading, setIsLoading] = useState(false);
  const router = useRouter();

  const getSupabaseClient = useCallback(() => {
    return createClient();
  }, []);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setIsLoading(true);

    if (form.password !== form.confirmPassword) {
      toast.error("Passwords do not match.");
      setIsLoading(false);
      return;
    }

    const supabase = getSupabaseClient();

    try {
      const { data, error } = await supabase.auth.signUp({
        email: form.email,
        password: form.password,
        options: {
          data: {
            full_name: `${form.firstName} ${form.lastName}`,
          },
        },
      });

      if (error) throw error;

      if (data.user) {
        toast.success("Account created successfully!");
        router.push(`/dashboard/${data.user.id}/text`);
      } else {
        throw new Error("Failed to create account. Please try again.");
      }
    } catch (error: any) {
      console.error("Error:", error);
      toast.error(
        error.error_description ||
          error.message ||
          "An error occurred during signup."
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="w-full lg:grid lg:min-h-[600px] lg:grid-cols-2 xl:min-h-[800px]">
      <div className="flex items-center justify-center py-12 px-4 lg:px-12">
        <div className="mx-auto grid w-full max-w-md gap-6">
          <div className="grid gap-2 text-center">
            <h1 className="text-3xl font-bold">Sign Up</h1>
            <p className="text-sm text-gray-500">
              Enter your information to create an account
            </p>
          </div>
          <form onSubmit={handleSubmit} className="grid gap-4">
            <div className="grid grid-cols-2 gap-4">
              <div className="grid gap-2">
                <Label htmlFor="firstName">First Name</Label>
                <Input
                  id="firstName"
                  name="firstName"
                  placeholder="John"
                  value={form.firstName}
                  onChange={handleChange}
                  required
                />
              </div>
              <div className="grid gap-2">
                <Label htmlFor="lastName">Last Name</Label>
                <Input
                  id="lastName"
                  name="lastName"
                  placeholder="Doe"
                  value={form.lastName}
                  onChange={handleChange}
                  required
                />
              </div>
            </div>
            <div className="grid gap-2">
              <Label htmlFor="email">Email</Label>
              <Input
                id="email"
                name="email"
                type="email"
                placeholder="m@example.com"
                value={form.email}
                onChange={handleChange}
                required
              />
            </div>
            <div className="grid gap-2">
              <Label htmlFor="password">Password</Label>
              <Input
                id="password"
                name="password"
                type="password"
                placeholder="********"
                value={form.password}
                onChange={handleChange}
                required
              />
            </div>
            <div className="grid gap-2">
              <Label htmlFor="confirmPassword">Confirm Password</Label>
              <Input
                id="confirmPassword"
                name="confirmPassword"
                type="password"
                placeholder="********"
                value={form.confirmPassword}
                onChange={handleChange}
                required
              />
            </div>
            <Button type="submit" className="w-full" disabled={isLoading}>
              {isLoading ? "Creating Account..." : "Create an Account"}
            </Button>
          </form>
          <div className="mt-4 text-center text-sm">
            Already have an account?{" "}
            <Link href="/login" className="underline">
              Log In
            </Link>
          </div>
        </div>
      </div>
      <div className="hidden lg:block bg-muted">
        <Image
          src="/imageSignup.jpg"
          alt="Signup Image"
          width="1920"
          height="1080"
          priority={true}
          className="h-screen w-full object-cover dark:brightness-[0.2] dark:grayscale"
        />
      </div>
      <Toaster position="top-center" />
    </div>
  );
}
