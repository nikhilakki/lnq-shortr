import type { NextPage } from 'next'
import Head from 'next/head'
import Image from 'next/image'

const Home: NextPage = () => {
  return (
    <div>
      <Head>
        <title>LNQ Shortr</title>
        <meta name="description" content="Link Shortener a.k.a LnQ Shortr" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <div>
        <h1>
          Welcome to <a href="https://nikhilakki.in">LnQ-Shortr!</a>
        </h1>
        </div>
      </main>

      <footer>
        <a
          href="https://nikhilakki.in"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by{' '}
          <span>
            <Image src="/vercel.svg" alt="lnq shortr Logo" width={72} height={16} />
          </span>
        </a>
      </footer>
    </div>
  )
}

export default Home
