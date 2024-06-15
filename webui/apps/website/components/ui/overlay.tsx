import React from "react";

interface Props {}

const Overlay: React.FC<React.PropsWithChildren<Props>> = ({ children }) => {
  console.log("Overlay");
  return (
    <div className="fixed inset-4 z-50 flex items-center justify-center bg-black bg-opacity-50">
      {children}
    </div>
  );
};

export { Overlay };
