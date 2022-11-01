// Copyright (c) 2022 Nikhil Akki
// 
// This software is released under the MIT License.
// https://opensource.org/licenses/MIT

import GitHubButton from 'react-github-btn'
const Fin = () => {
    return (
        <section id="fin" className="bg-white dark:bg-gray-900">
            <div className="py-8 px-4 mx-auto max-w-screen-xl sm:py-16 lg:px-6">
                <div className="mx-auto max-w-screen-sm text-center">
                    <h2 className="mb-4 text-4xl font-extrabold leading-tight text-gray-900 dark:text-white">We are Open Source!</h2>
                    <p className="mb-6 font-light text-gray-500 dark:text-gray-400 md:text-lg">Check out our GitHub page to know more, give us a 🌟 if you like our work!</p>
                    {/* <a href="https://github.com/nikhilakki/lnq-shortr" className="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800" rel="noreferrer">Let&apos;s go!</a> */}
                    <GitHubButton href="https://github.com/nikhilakki/lnq-shortr" data-color-scheme="no-preference: light; light: light; dark: dark;" data-icon="octicon-star" data-size="large" data-show-count="true" aria-label="Star nikhilakki/lnq-shortr on GitHub">Star</GitHubButton>
                </div>
            </div>
        </section>
    );
};

export default Fin;