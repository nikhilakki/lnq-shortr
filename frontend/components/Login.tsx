import { useSession, signIn, signOut } from "next-auth/react"

export default function Login() {
    const { data: session } = useSession()
    if (session) {
        return (
            <>
                Signed in as {session.user.email} <br />
                <button className='btn btn-danger' onClick={() => signOut()}>Logout</button>
            </>
        )
    }
    return (
        <>
            {/* Not signed in <br /> */}
            <button className='btn btn-primary' onClick={() => signIn()}>Login</button>
        </>
    )
}