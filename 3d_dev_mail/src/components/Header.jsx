import 'boxicons/css/boxicons.min.css'

const Header = () => {
  
  // Function to toggle the mobile menu  
  const toggleMobileMenu = () => {
    
    // Get the mobile menu element    
    const mobileMenu = document.getElementById('mobileMenu')
    
    // Toggle the 'hidden' class to show/hide the menu    
    if (mobileMenu.classList.contains('hidden')) {
      mobileMenu.classList.remove('hidden');
    } else {
      mobileMenu.classList.add('hidden');
    }
  }

  return (
    <header className="flex justify-between items-center py-4 px-4 lg:px-20">
      
        <h1 data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1500">
          Larchitek's Dev Mail
        </h1>
      
      {/* Desktop Navigation */}
        <nav className="hidden md:flex items-center gap-12">
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1000" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">HOME</a>
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1500" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">BLOG</a>
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="2000" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">LOGIN</a>
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="2500" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">SIGNUP</a>
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="3000" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">HELP</a>
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="3500" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">FAQ</a>
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="4000" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">GITHUB</a>
      </nav>
      <nav className="hidden md:flex items-center gap-12">
        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1500" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">COMPANY</a>

        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1500" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">FEATURES</a>

        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1500" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">RESOURCES</a>

        <a data-aos="fade-down" data-aos-easing="linear" data-aos-duration="1500" className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">DOCS</a>
      </nav>

      <button className='hidden md:block bg-[#a7a7a7] text-black py-3 px-8 rounded-full border-none font-medium text-base transition-colors hover:bg-gray-300'>
        SIGNIN
      </button>

      {/* Mobile Menu button - Visible only on Mobile */}

      <button onClick={toggleMobileMenu} className="md:hidden text-3xl p-2 z-50">
        <i className="bx bx-menu"></i>
      </button>

      {/* Mobile Menu - Hidden by default */}

      <div id="mobileMenu" className="hidden fixed top-16 bottom-0 left-0 right-0 p-5 md:hidden z-40 bg-black bg-opacity-70 backdrop-blur-md">
        <nav className="flex flex-col gap-6 items-center">
        <a className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">COMPANY</a>
        
        <a className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">FEATURES</a>
        
        <a className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">RESOURCES</a>
        
        <a className="text-base tracking-wider transition-colors hover:text-gray-300 z-50" href="#">DOCS</a>
        </nav>
      </div>
    </header>
  )
}

export default Header