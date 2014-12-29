#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Ud T
# Generated: Wed Dec 17 19:43:08 2014
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from grc_gnuradio import blks2 as grc_blks2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class UD_T(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Ud T")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.transistion = transistion = 100
		self.sps = sps = 9
		self.sideband_rx = sideband_rx = 1000
		self.sideband = sideband = 1000
		self.samp_rate = samp_rate = 48000
		self.payload = payload = 5
		self.interpolation = interpolation = 500
		self.carrier = carrier = 23000

		##################################################
		# Blocks
		##################################################
		self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0_0.win)
		self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(1, (firdes.band_pass (0.50,samp_rate,carrier-sideband,carrier+sideband,transistion)), -carrier, samp_rate)
		self.digital_gfsk_mod_0 = digital.gfsk_mod(
			samples_per_symbol=sps,
			sensitivity=1.0,
			bt=0.35,
			verbose=False,
			log=False,
		)
		self.blocks_complex_to_real_0 = blocks.complex_to_real(1)
		self.blks2_tcp_source_0 = grc_blks2.tcp_source(
			itemsize=gr.sizeof_char*1,
			addr="127.0.0.1",
			port=10004,
			server=True,
		)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_ccc(
			interpolation=500,
			decimation=1,
			taps=None,
			fractional_bw=None,
		)
		self.blks2_packet_encoder_0 = grc_blks2.packet_mod_b(grc_blks2.packet_encoder(
				samples_per_symbol=sps,
				bits_per_symbol=1,
				access_code="",
				pad_for_usrp=False,
			),
			payload_length=payload,
		)
		self.audio_sink_0 = audio.sink(48000, "", True)

		##################################################
		# Connections
		##################################################
		self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_complex_to_real_0, 0))
		self.connect((self.blks2_packet_encoder_0, 0), (self.digital_gfsk_mod_0, 0))
		self.connect((self.digital_gfsk_mod_0, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))
		self.connect((self.blks2_tcp_source_0, 0), (self.blks2_packet_encoder_0, 0))
		self.connect((self.blocks_complex_to_real_0, 0), (self.audio_sink_0, 0))
		self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.wxgui_fftsink2_0_0, 0))


	def get_transistion(self):
		return self.transistion

	def set_transistion(self, transistion):
		self.transistion = transistion
		self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.band_pass (0.50,self.samp_rate,self.carrier-self.sideband,self.carrier+self.sideband,self.transistion)))

	def get_sps(self):
		return self.sps

	def set_sps(self, sps):
		self.sps = sps

	def get_sideband_rx(self):
		return self.sideband_rx

	def set_sideband_rx(self, sideband_rx):
		self.sideband_rx = sideband_rx

	def get_sideband(self):
		return self.sideband

	def set_sideband(self, sideband):
		self.sideband = sideband
		self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.band_pass (0.50,self.samp_rate,self.carrier-self.sideband,self.carrier+self.sideband,self.transistion)))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.band_pass (0.50,self.samp_rate,self.carrier-self.sideband,self.carrier+self.sideband,self.transistion)))
		self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)

	def get_payload(self):
		return self.payload

	def set_payload(self, payload):
		self.payload = payload

	def get_interpolation(self):
		return self.interpolation

	def set_interpolation(self, interpolation):
		self.interpolation = interpolation

	def get_carrier(self):
		return self.carrier

	def set_carrier(self, carrier):
		self.carrier = carrier
		self.freq_xlating_fir_filter_xxx_0.set_taps((firdes.band_pass (0.50,self.samp_rate,self.carrier-self.sideband,self.carrier+self.sideband,self.transistion)))
		self.freq_xlating_fir_filter_xxx_0.set_center_freq(-self.carrier)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = UD_T()
	tb.Run(True)

