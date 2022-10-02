import './Login.css'

export default function LoginPage() {
    return (<div className='login-container1'>
        <svg className="bg-desktop" preserveAspectRatio="xMidYMid slice"
            width="1780" height="1085" viewBox="0 0 1780 1085" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="469" y="-36" width="1312" height="1187" fill="#E1E1E1" />
            <ellipse cx="-926.5" cy="492" rx="1874.5" ry="1851" fill="#252221" />
            <ellipse cx="-926.5" cy="492" rx="1874.5" ry="1851" fill="url(#paint0_radial)" />
            <defs>
                <radialGradient id="paint0_radial" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(-927 492) scale(2015.56 1441.26)">
                    <stop offset="0.802083" stopColor="#325987" />
                    <stop offset="1" stopColor="#23466F" />
                </radialGradient>
            </defs>
        </svg>

        <svg className="bg-phone"
            width="841" height="1596" viewBox="0 0 841 1596" fill="none" xmlns="http://www.w3.org/2000/svg">
            <rect x="-203" y="636" width="1312" height="1187" fill="#E1E1E1" />
            <ellipse cx="432" cy="-1196" rx="1929" ry="1905" fill="#252221" />
            <ellipse cx="432" cy="-1196" rx="1929" ry="1905" fill="url(#paint1_radial)" />
            <defs>
                <radialGradient id="paint1_radial" cx="0" cy="0" r="1" gradientUnits="userSpaceOnUse" gradientTransform="translate(431.485 -1196) scale(2074.17 1483.3)">
                    <stop offset="0.802083" stopColor="#325987" />
                    <stop offset="1" stopColor="#23466F" />
                </radialGradient>
            </defs>
        </svg>

        <div className="login-container">
            <div className="cta">
                <img src="/movify-sm.png" />
                <h1>Movify</h1>
                <p>The social network for cinephiles</p>
                <div className="login">
                    <a href="/api/login" className="primary">Sign up</a>
                    <a href="/api/login" className="secondary">Sign in</a>
                </div>

            </div>
            <div className="infos">
                <div className="blabla">
                    This is an entry for Build on Redis 21.
                    <br /><br />
                    Feel free to poke around and try all functionalities, a lot of love and effort were put into making it all work together :)
                    <br /><br />
                    This website was built on RedisGraph.
                </div>
            </div>
        </div>
    </div>)
}