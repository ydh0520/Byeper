export interface AllPlayListModule {
  AllPlayList: PlayList[] | null;
}

export interface PlayList {
  playlistId: number | null;
  playlistTitle: string | null;
  playlistDescription: string | null;
  userId: string | null;
  playlistType: number | null;
  playlistCategory: number | null;
  playlistLevel: number | null;
  playlistImg: string | null;
}
