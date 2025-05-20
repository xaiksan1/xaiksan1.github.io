import 'boxicons/css/boxicons.min.css'
import Spline from '@splinetool/react-spline';


const Hero = () => {
return (
    <main className="flex lg:mt-20 flex-col lg:flex-row items-center justify-between min-h-[calc(90vh-6rem)]">
        {/* Left side - Text and button */}      
        <div data-aos="fade-right" data-aos-offset="300" data-aos-easing="ease-in-sine" className="max-w-xl ml-[5%] z-10 mt-[90%] md:mt-[60%] lg:mt-0">
            {/* Tag box-with gradient border */}
            <div className='relative w-[95%] rounded-full sm:w-48 h-10 bg-gradient-to-r from-[#656565] to-[#e99b63] shadow-[0_0_15px_rgba(233,155,99,0.5)]'>
                <div className='absolute inset-[3px] bg-black rounded-full flex items-center justify-center gap-1'>
                    <i className='bx bx-diamond'></i>
                    INTRODUCING
                </div>                
            </div>

            {/* Main Heading */}
            <h1 className='text-3-xl sm:text-4xl md:text-5xl lg:text-6xl font-semibold tracking-wider my-8'>
                EMAIL FOR
                <br />
                <span className='text-[#e9bf63]'>  DEVELOPERS  </span>
                <br />
                <span className='text-[#e99b63]'>    BY DEVELOPERS</span>
                <br />
                <span className='text-[#656565]'>      FOR DEVELOPERS</span>
            </h1>

            {/* Description */}
            <p className='text-lg sm:text-xl lg:text-2xl font-light tracking-wider text-[#656565] max-w-2xl mb-8'>
                A powerful email service designed specifically for developers. 
                With our API, you can easily integrate email functionality into your applications.
                <br />
                <span className='text-[#e9bf63]'>  Get started today and experience the difference!</span>
            </p>

            {/* Button */}
            <div className='flex gap-4 mt-8'>
                <a className='border border-[#2a2a2a] py-2 sm:py-3 px-4 sm:px-5 rounded-full sm:text-lg text-sm font-semibold tracking-wider transition-all duration-300 hover:bg-[#1a1a1a]' href="#">
                    Documentation <i class='bx bx-link-external'></i>
                </a>

                <a className='border border-[#2a2a2a] py-2 sm:py-3 px-4 sm:px-5 rounded-full sm:text-lg text-sm font-semibold tracking-wider transition-all duration-300 hover:bg-[#1a1a1a] bg-gray-300 text-black hover:text-white' href="#">
                    Get Started <i class='bx bx-link-external'></i>
                </a>
            </div>
        </div> {/* This div now correctly closes the "Left side" container that started with className="max-w-xl..." */}

        {/* Right side - Image */}
        <div className="hidden lg:block">
            <img src="/path/to/your/image.jpg" alt="Hero Image" className="max-w-full h-auto" />
        </div>

        {/* 3D Robot */}
        <Spline data-aos="fade-zoom-in" data-aos-easing="ease-in-back" data-aos-delay="300" data-aos-offset="0" data-aos-duration="3000" className='absolute lg:top-0 top-[-20%] bottom-0 lg:left-[25%] sm:left-[-2%] h-full' scene="https://prod.spline.design/eVISDvYgugPpQ1hg/scene.splinecode" />

    </main>
);
};
export default Hero;