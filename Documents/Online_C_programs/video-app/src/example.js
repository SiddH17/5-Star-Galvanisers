import { ReactMediaRecorder, reactMediaRecorder } from "react-media-recorder";

function player()   {
    return (
        <>
          <ReactMediaRecorder
            video
            render={({ status, startRecording, stopRecording, mediaBlobUrl }) => (
              <div>
                <p>{status}</p>
                <button className="btn btn-primary" onClick={startRecording}>
                  Start Recording
                </button>
                <button className="btn btn-primary" onClick={stopRecording}>
                  Stop Recording
                </button>
                <video src={mediaBlobUrl} controls autoPlay />
              </div>
            )}
          />
        </>
      );
}

export default player;