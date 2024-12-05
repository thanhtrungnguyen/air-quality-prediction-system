import { Component } from '@angular/core';
import { AirQuality } from '../../model/defind.model';

@Component({
  selector: 'app-air-quality-detail',
  templateUrl: './air-quality-detail.component.html',
  styleUrl: './air-quality-detail.component.css'
})
export class AirQualityDetailComponent {
  maxValues = {
    'PM2.5': 100,
    PM10: 100,
    O3: 100,
    NO2: 100,
    CO: 2000,
  };

  aqi = 230;
  airQuality: AirQuality = {
    aqi: this.aqi,
    icon: this.getAQIDetails(this.aqi).icon,
    status: this.getAQIDetails(this.aqi).advice,
    color: this.getAQIDetails(this.aqi).color,
    pollutants: [
      {
        name: 'PM2.5',
        value: 80,
        unit: 'µg/m³',
        percentage: (80 / this.maxValues['PM2.5']) * 100,
      },
      {
        name: 'PM10',
        value: 22.6,
        unit: 'µg/m³',
        percentage: (22.6 / this.maxValues['PM10']) * 100,
      },
      {
        name: 'O3',
        value: 16,
        unit: 'µg/m³',
        percentage: (16 / this.maxValues['O3']) * 100,
      },
      {
        name: 'NO2',
        value: 42,
        unit: 'µg/m³',
        percentage: (42 / this.maxValues['NO2']) * 100,
      },
      {
        name: 'CO',
        value: 1112.9,
        unit: 'µg/m³',
        percentage: (1112.9 / this.maxValues['CO']) * 100,
      },
    ],
    recommendations: [
      { icon: '🏃‍♂️', text: 'Tránh tập thể dục ngoài trời' },
      { icon: '😷', text: 'Đeo mặt nạ khi ra ngoài', link: 'MUA MẶT NẠ' },
      {
        icon: '🚪',
        text: 'Đóng cửa sổ để tránh không khí bẩn bên ngoài',
        link: 'MUA MỘT TRÌNH THEO DÕI',
      },
      {
        icon: '💨',
        text: 'Chạy máy lọc không khí',
        link: 'MUA MÁY LỌC KHÔNG KHÍ',
      },
    ],
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
}
