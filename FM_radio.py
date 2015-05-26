#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Fm Radio
# Generated: Wed May 20 20:02:29 2015
##################################################

from gnuradio import audio
from gnuradio import blks2
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import osmosdr
import wx

class FM_radio(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Fm Radio")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.volume = volume = 1
		self.samp_rate = samp_rate = 2.7e6
		self.freq = freq = 89.7e6

		##################################################
		# Blocks
		##################################################
		_volume_sizer = wx.BoxSizer(wx.VERTICAL)
		self._volume_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			label="Volume",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._volume_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_volume_sizer,
			value=self.volume,
			callback=self.set_volume,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_volume_sizer)
		self._freq_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.freq,
			callback=self.set_freq,
			label='freq',
			converter=forms.float_converter(),
		)
		self.Add(self._freq_text_box)
		self.rtlsdr_source_c_0 = osmosdr.source_c( args="nchan=" + str(1) + " " + "" )
		self.rtlsdr_source_c_0.set_sample_rate(samp_rate)
		self.rtlsdr_source_c_0.set_center_freq(freq, 0)
		self.rtlsdr_source_c_0.set_freq_corr(0, 0)
		self.rtlsdr_source_c_0.set_dc_offset_mode(0, 0)
		self.rtlsdr_source_c_0.set_iq_balance_mode(0, 0)
		self.rtlsdr_source_c_0.set_gain_mode(0, 0)
		self.rtlsdr_source_c_0.set_gain(20, 0)
		self.rtlsdr_source_c_0.set_if_gain(20, 0)
		self.rtlsdr_source_c_0.set_bb_gain(20, 0)
		self.rtlsdr_source_c_0.set_antenna("", 0)
		self.rtlsdr_source_c_0.set_bandwidth(0, 0)
		  
		self.low_pass_filter_0 = gr.fir_filter_ccf(int(samp_rate/200e3), firdes.low_pass(
			1, samp_rate, 100e3, 1e6, firdes.WIN_HAMMING, 6.76))
		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((volume, ))
		self.blks2_wfm_rcv_0 = blks2.wfm_rcv(
			quad_rate=200e3,
			audio_decimation=1,
		)
		self.blks2_rational_resampler_xxx_0 = blks2.rational_resampler_fff(
			interpolation=48,
			decimation=200,
			taps=None,
			fractional_bw=None,
		)
		self.audio_sink_0 = audio.sink(48000, "", False)

		##################################################
		# Connections
		##################################################
		self.connect((self.blks2_wfm_rcv_0, 0), (self.blks2_rational_resampler_xxx_0, 0))
		self.connect((self.rtlsdr_source_c_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.blks2_wfm_rcv_0, 0))
		self.connect((self.blks2_rational_resampler_xxx_0, 0), (self.blocks_multiply_const_vxx_0, 0))
		self.connect((self.blocks_multiply_const_vxx_0, 0), (self.audio_sink_0, 0))


	def get_volume(self):
		return self.volume

	def set_volume(self, volume):
		self.volume = volume
		self._volume_slider.set_value(self.volume)
		self._volume_text_box.set_value(self.volume)
		self.blocks_multiply_const_vxx_0.set_k((self.volume, ))

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.rtlsdr_source_c_0.set_sample_rate(self.samp_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 100e3, 1e6, firdes.WIN_HAMMING, 6.76))

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self.rtlsdr_source_c_0.set_center_freq(self.freq, 0)
		self._freq_text_box.set_value(self.freq)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = FM_radio()
	tb.Run(True)

