import Header from "./components/Header"
import Hero from "./components/Hero"
import AOS from "aos"
import "aos/dist/aos.css"
import { useEffect } from "react"

export default function App() {
  useEffect(() => {
    AOS.init({
      duration: 1500,
      easing: "ease-in-out",
      once: true,
      mirror: false,
      offset: 100,
      delay: 0,
      disable: "mobile",
    })
    AOS.refresh();
  }, []);

  return (
    <main>
      {/* Gradient image */}
      <img className="absolute top-0 right-0 opacity-60 -z-1" src="/gradient.png" alt="gradient-img" />
    
      {/* Blur Effect */}
      <div className="h-0 w-[40rem] absolute top-[20%] right-[-5%] shadow-[0_0_900px_20px_#e99b63]-rotate-[30deg] -z-10"></div>

      <Header />
      <Hero />
    </main>
  )
}
