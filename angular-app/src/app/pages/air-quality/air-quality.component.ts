import { Component } from '@angular/core';

import { NgClass, NgFor, NgStyle } from '@angular/common';
import { AirQuality, Recommendation } from '../../models/defind.model';
@Component({
  selector: 'app-air-quality',
  standalone: true,
  imports: [NgFor, NgClass, NgStyle],
  templateUrl: './air-quality.component.html',
  styleUrl: './air-quality.component.css',
})
export class AirQualityComponent {
  data = {
    aqi: 340,
    pollutants: [
      {
        name: 'PM2.5',
        value: 80,
      },
      {
        name: 'PM10',
        value: 22.6,
      },
      {
        name: 'O3',
        value: 16,
      },
      {
        name: 'NO2',
        value: 42,
      },
      {
        name: 'CO',
        value: 900,
      },
    ],
  }

  maxValues = {
    'PM2.5': 100,
    PM10: 100,
    O3: 100,
    NO2: 100,
    CO: 2000,
  };

  airQuality: AirQuality = {
    aqi: this.data.aqi,
    icon: this.getAQIDetails(this.data.aqi).icon,
    status: this.getAQIDetails(this.data.aqi).advice,
    color: this.getAQIDetails(this.data.aqi).color,
    pollutants: [
      {
        name: 'PM2.5',
        value: this.data.pollutants[0].value,
        unit: 'µg/m³',
        percentage: (this.data.pollutants[0].value / this.maxValues['PM2.5']) * 100,
      },
      {
        name: 'PM10',
        value: this.data.pollutants[1].value,
        unit: 'µg/m³',
        percentage: (this.data.pollutants[1].value / this.maxValues['PM10']) * 100,
      },
      {
        name: 'O3',
        value: this.data.pollutants[2].value,
        unit: 'µg/m³',
        percentage: (this.data.pollutants[2].value / this.maxValues['O3']) * 100,
      },
      {
        name: 'NO2',
        value: this.data.pollutants[3].value,
        unit: 'µg/m³',
        percentage: (this.data.pollutants[3].value / this.maxValues['NO2']) * 100,
      },
      {
        name: 'CO',
        value: this.data.pollutants[4].value,
        unit: 'µg/m³',
        percentage: (this.data.pollutants[4].value / this.maxValues['CO']) * 100,
      },
    ],
    recommendations: this.getRecommendations(this.data.aqi) as Recommendation[],
  };

  getAQIDetails(aqi: number): {
    advice: string;
    healthEffects: string;
    actions: string;
    color: string;
    icon: string;
  } {
    if (aqi <= 50) {
      return {
        advice: 'Chất lượng không khí tốt.',
        healthEffects: 'Không có tác động sức khỏe nào.',
        actions: 'Bạn có thể ra ngoài và tận hưởng không khí trong lành!',
        color: 'green',
        icon: 'https://www.iqair.com/dl/web/aqi/ic_face_48_green.svg',
      };
    } else if (aqi <= 100) {
      return {
        advice: 'Chất lượng không khí chấp nhận được.',
        healthEffects: 'Một số người nhạy cảm có thể gặp vấn đề nhẹ.',
        actions: 'Không cần thay đổi hoạt động thường ngày.',
        color: 'yellow',
        icon: 'https://www.iqair.com/dl/web/aqi/ic_face_48_yellow.svg',
      };
    } else if (aqi <= 150) {
      return {
        advice: 'Không lành mạnh cho nhóm nhạy cảm.',
        healthEffects: 'Những người nhạy cảm có thể gặp vấn đề sức khỏe.',
        actions: 'Hạn chế hoạt động ngoài trời cho nhóm nhạy cảm.',
        color: 'orange',
        icon: 'https://www.iqair.com/dl/web/aqi/ic_face_48_orange.svg',
      };
    } else if (aqi <= 200) {
      return {
        advice: 'Không lành mạnh.',
        healthEffects: 'Mọi người có thể bắt đầu gặp vấn đề sức khỏe.',
        actions: 'Hạn chế ra ngoài và giảm hoạt động mạnh.',
        color: '#ff6b6b',
        icon: 'https://www.iqair.com/dl/web/aqi/ic_face_48_red.svg',
      };
    } else if (aqi <= 300) {
      return {
        advice: 'Rất không lành mạnh.',
        healthEffects: 'Tác động sức khỏe nghiêm trọng hơn có thể xảy ra.',
        actions: 'Tránh ra ngoài nếu có thể.',
        color: 'purple',
        icon: 'https://www.iqair.com/dl/web/aqi/ic_face_48_purple.svg',
      };
    } else {
      return {
        advice: 'Nguy hiểm.',
        healthEffects: 'Tất cả mọi người có thể bị ảnh hưởng sức khỏe.',
        actions: 'Ở trong nhà và đóng kín cửa.',
        color: 'maroon',
        icon: 'https://www.iqair.com/dl/web/aqi/ic_face_48_maroon.svg',
      };
    }
  }

  getRecommendations(aqi: number): {icon?: string; text: string; link?: string }[] {
    var defaultIcon = '😀';

    if (aqi <= 50) {
      defaultIcon = '😀';
      return [
        { text: 'Không cần thay đổi hoạt động thường ngày.', icon: defaultIcon },
        { text: 'Tận hưởng không khí trong lành.', icon: defaultIcon },
        { text: 'Đi dạo ngoài trời.', icon: defaultIcon },
        { text: 'Mở cửa sổ để thông gió.', icon: defaultIcon }
      ];
    } else if (aqi <= 100) {
      defaultIcon = '🙂';
      return [
        { text: 'Một số người nhạy cảm có thể gặp vấn đề nhẹ.', icon: defaultIcon },
        { text: 'Tiếp tục các hoạt động ngoài trời.', icon: defaultIcon },
        { text: 'Theo dõi chất lượng không khí.', icon: defaultIcon },
        { text: 'Giữ cửa sổ mở nếu không khí trong lành.', icon: defaultIcon }
      ];
    } else if (aqi <= 150) {
      defaultIcon = '😕';
      return [
        { text: 'Hạn chế hoạt động ngoài trời cho nhóm nhạy cảm.', icon: defaultIcon },
        { text: 'Đeo mặt nạ khi ra ngoài.', icon: 'MUA MẶT NẠ' },
        { text: 'Tránh các hoạt động thể chất mạnh.', icon: defaultIcon },
        { text: 'Theo dõi sức khỏe nếu cảm thấy không khỏe.', icon: defaultIcon }
      ];
    } else if (aqi <= 200) {
      defaultIcon = '😏';
      return [
        { text: 'Hạn chế ra ngoài và giảm hoạt động mạnh.', icon: defaultIcon },
        { text: 'Đóng cửa sổ để tránh không khí bẩn bên ngoài.', icon: defaultIcon },
        { text: 'Chạy máy lọc không khí.', icon: defaultIcon },
        { text: 'Tránh các khu vực có nhiều khói bụi.', icon: defaultIcon }
      ];
    } else if (aqi <= 300) {
      defaultIcon = '😞';
      return [
        { text: 'Tránh ra ngoài nếu có thể.', icon: defaultIcon },
        { text: 'Sử dụng máy lọc không khí trong nhà.', icon: defaultIcon },
        { text: 'Đóng kín cửa sổ và cửa ra vào.', icon: defaultIcon },
        { text: 'Theo dõi sức khỏe và tìm kiếm sự giúp đỡ nếu cần.', icon: defaultIcon }
      ];
    } else {
      defaultIcon = '🫠';
      return [
        { text: 'Ở trong nhà và đóng kín cửa.', icon: defaultIcon },
        { text: 'Tránh mọi hoạt động ngoài trời.', icon: defaultIcon },
        { text: 'Sử dụng máy lọc không khí.', icon: defaultIcon },
        { text: 'Liên hệ với cơ quan y tế nếu có triệu chứng.', icon: defaultIcon }
      ];
    }
  }
}
