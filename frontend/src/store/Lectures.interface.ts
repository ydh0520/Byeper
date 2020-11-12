export interface LecturesModule {
  lectures: Lecture[];
  allCaptureImgs: CaptureImages[];
  courses: Course[];
}

export interface Lecture {
  video_id: string;
  play_log: number;
  video_description: string;
  video_max_img: number;
  play_complete: number;
  video_title: string;
  play_note: string;
  video_img: string;
  play_id: number;
  playlist_id: number;
}

export interface CaptureImages {
  address: string;
  time: number;
  diff: number;
}

export interface Course {
  playlistId: number;
  playlistTitle: string;
  playlistDescription: string;
  userId: string;
  playlistType: number;
  playlistCategory: number;
  playlistLevel: number;
  playlistImg: string;
}
