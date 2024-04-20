import { useState } from 'react'
import { Input } from './ui/input'
import { Button } from './ui/button'
import Modal from 'react-modal'

const customStyles = {
  content: {
    top: '50%',
    left: '50%',
    right: 'auto',
    bottom: 'auto',
    marginRight: '-50%',
    transform: 'translate(-50%, -50%)',
  },
}

const Adddata = () => {
  const [isOpen, setIsOpen] = useState(false)

  const openModal = () => {
    setIsOpen(true)
  }

  const closeModal = () => {
    setIsOpen(false)
  }

  const handleFileUpload = (event: any) => {
    const file = event.target.files[0]
    // Handle the file upload logic here
  }

  return (
    <div>
      <Button onClick={openModal}>Open Form</Button>
      <Modal isOpen={isOpen} onRequestClose={closeModal} style={customStyles} contentLabel="Example Modal">
        <div className="bg-white rounded-lg p-8">
          <h2 className="text-2xl mb-4">Upload File</h2>
          <Input type="file" onChange={handleFileUpload} />
          <div className="mt-4">
            <Button onClick={closeModal}>Close</Button>
            <Button type="submit" className="ml-2" onClick={closeModal}>
              Upload
            </Button>
          </div>
        </div>
      </Modal>
    </div>
  )
}

export default Adddata
