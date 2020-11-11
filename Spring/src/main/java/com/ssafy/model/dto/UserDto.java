package com.ssafy.model.dto;

import java.io.Serializable;

import javax.persistence.Column;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Table(name = "user")
public class UserDto implements Serializable {
	@Id
	@Column(name = "user_id")
	private String userId;

	@Column(name = "user_password")
	private String userPassword;

	@Column(name = "user_name")
	private String userName;

	@Column(name = "user_type")
	private int userType;

	@Column(name = "user_channel_id")
	private String channelId;

	public String getUserId() {
		return userId;
	}

	public void setUserId(String userId) {
		this.userId = userId;
	}

	public String getUserPassword() {
		return userPassword;
	}

	public void setUserPassword(String userPassword) {
		this.userPassword = userPassword;
	}

	public String getUserName() {
		return userName;
	}

	public void setUserName(String userName) {
		this.userName = userName;
	}

	public int getUserType() {
		return userType;
	}

	public void setUserType(int userType) {
		this.userType = userType;
	}

	public String getChannelId() {
		return channelId;
	}

	public void setChannelId(String channelId) {
		this.channelId = channelId;
	}

	@Override
	public String toString() {
		return "UserDto [userId=" + userId + ", userPassword=" + userPassword + ", userName=" + userName + ", userType="
				+ userType + ", channelId=" + channelId + "]";
	}

}
