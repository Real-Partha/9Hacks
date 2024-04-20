interface ContentCardProps {
  heading: string
  data: any
  date: any
}

const ContentCard = (props: ContentCardProps) => {
  return (
    <div className="w-[90%] border border-white h-[100px] text-white">
      <div className="flex justify-between items-center p-2">
        <div className="font-bold">{props.heading}</div>
        <div className="font-thin text-sm">{props.date}</div>
      </div>

      <div className="text-sm font-thin p-1">{props.data}</div>
    </div>
  )
}

export default ContentCard
