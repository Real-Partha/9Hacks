import { Link } from 'react-router-dom'
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar'
import { Button } from './ui/button'

import ContentCard from './ContentCard'
import Adddata from './Adddata'
import { useState } from 'react'
import Dairy from './Dairy'

const Landing = ({ logout }: { logout: () => void }) => {
  const [dairy, setDairy] = useState(false)
  const render = () => {
    setDairy(true)
  }
  return (
    <div className="bg-[#0F0F0F] h-screen w-full flex">
      <div className="bg-[#1c1e20] justify-between w-1/6 h-full flex flex-col">
        <Link to={'/home'}>
          <div className="logo-header flex p-5  items-center  text-white ">
            <Avatar style={{ height: '50px', width: '50px' }}>
              <AvatarImage src="https://github.com/shadcn.png" />
              <AvatarFallback>CN</AvatarFallback>
            </Avatar>
            <h1 className=" text-[30px] pl-5 font-custom">Nostalgia</h1>
          </div>
        </Link>

        <Button className="" onClick={logout}>
          Logout
        </Button>
      </div>
      <div className="bg-[#0F0F0F] h-full w-1/6 ">
        {' '}
        <ContentCard {...{ heading: '9 Hacks', data: 'this is dummy data', date: '20/4/24' }} />
      </div>
      <div className="4/6 flex flex-col">
        <div className="h-[50px] w-full flex p-5 ">
          {' '}
          <Button className="ml-[900px]">
            <Adddata />
          </Button>{' '}
        </div>
        <div className="h-full mt-8">{dairy && <Dairy />}</div>
      </div>
    </div>
  )
}

export default Landing
