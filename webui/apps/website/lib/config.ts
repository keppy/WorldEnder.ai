export const config = {
  apiServer: process.env.NEXT_PUBLIC_API_SERVER,
  pingInterval: parseInt(process.env.NEXT_PUBLIC_PING_INTERVAL ?? "5000"),
};
