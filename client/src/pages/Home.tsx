import { FcGoogle } from 'react-icons/fc'

import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'

import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'

import React, { useState, useEffect } from 'react'
import { googleLogout, useGoogleLogin, CodeResponse } from '@react-oauth/google'
import axios from 'axios'

interface UserProfile {
  picture: string
  name: string
  email: string
}

interface ExtendedCodeResponse extends CodeResponse {
  access_token: string
}

const Home: React.FC = () => {
  const [user, setUser] = useState<ExtendedCodeResponse | null>(null)
  const [profile, setProfile] = useState<UserProfile | null>(null)
  const [tokenData, setTokenData] = useState<{
    token: string
    token_uri: string
    client_id: string
    client_secret: string
    scopes: string
    account: string
    expiry: string
  } | null>(null)

  const login = useGoogleLogin({
    onSuccess: (codeResponse: CodeResponse) => setUser(codeResponse as ExtendedCodeResponse),
    onError: (error) => console.log('Login Failed:', error),
    scope: 'https://www.googleapis.com/auth/photoslibrary https://www.googleapis.com/auth/calendar',
  })

  useEffect(() => {
    if (user) {
      axios
        .get(`https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=${user.access_token}`)
        .then((res) => {
          const { access_token } = user
          console.log(res)
          setTokenData({
            token: access_token,
            token_uri: 'https://oauth2.googleapis.com/token',
            client_id: 'YOUR_CLIENT_ID',
            client_secret: 'YOUR_CLIENT_SECRET',
            scopes: user.scope || '',
            account: '',
            expiry: new Date(Date.now() + 3600 * 1000).toISOString(), // Default expiry: 1 hour
          })
        })
        .catch((err) => console.log(err))
    }
  }, [user])

  useEffect(() => {
    if (user) {
      axios
        .get<UserProfile>(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
          headers: {
            Authorization: `Bearer ${user.access_token}`,
            Accept: 'application/json',
          },
        })
        .then((res) => {
          setProfile(res.data)
        })
        .catch((err) => console.log(err))
    }
  }, [user])

  const logOut = () => {
    googleLogout()
    setProfile(null)
  }

  return (
    <div>
      {profile ? (
        <div>
          <img src={profile.picture} alt="user image" />
          <h3>User Logged in</h3>
          <p>Name: {profile.name}</p>
          <p>Email Address: {profile.email}</p>
          <br />
          <br />
          {tokenData && (
            <div>
              <p>Token: {tokenData.token}</p>
              <p>Token URI: {tokenData.token_uri}</p>
              <p>Client ID: {tokenData.client_id}</p>
              <p>Client Secret: {tokenData.client_secret}</p>
              <p>Scopes: {tokenData.scopes}</p>
              <p>Expiry: {tokenData.expiry}</p>
            </div>
          )}
          <button onClick={logOut}>Log out</button>
        </div>
      ) : (
        <div className="flex flex-col border-slate-100 items-center h-[100vh] justify-center">
          <div>
            <Avatar style={{ height: '150px', width: '150px' }}>
              <AvatarImage src="https://github.com/shadcn.png" />
              <AvatarFallback>CN</AvatarFallback>
            </Avatar>
          </div>
          <Card style={{ width: '300px', height: '300px' }}>
            <CardHeader>
              <CardTitle>Login</CardTitle>
            </CardHeader>
            <div className="text-[50px] font-custom text-[var(--text-color)]">
              <h1>9 Hacks</h1>
            </div>
            <CardContent className=" flex justify-center ">
              <Button onClick={() => login()} className="bg-transparent h-10 gap-3">
                <FcGoogle size={30} />
                Login with Google
              </Button>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  )
}

export default Home
