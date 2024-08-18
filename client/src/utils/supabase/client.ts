import {
  createClient as _createClient,
  SupabaseClient,
} from "@supabase/supabase-js";

let supabaseInstance: SupabaseClient | null = null;

export const createClient = () => {
  if (!supabaseInstance) {
    supabaseInstance = _createClient(
      process.env.NEXT_PUBLIC_SUPABASE_URL!,
      process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
    );
  }
  return supabaseInstance;
};
