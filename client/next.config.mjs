/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
	console.log('API URL:', process.env.NEXT_PUBLIC_API_URL); // Add this line to verify
	return [
	  {
		source: '/complaint/:path*',
		destination: `${process.env.NEXT_PUBLIC_API_URL}complaint/:path*`, // Proxy to Backend
	  },
	];
  },
};

export default nextConfig;
