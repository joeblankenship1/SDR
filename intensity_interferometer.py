#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Intensity Interferometer
# Generated: Wed Mar 19 20:41:17 2014
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class intensity_interferometer(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Intensity Interferometer")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 250e3
		self.magnitude = magnitude = 0.05
		self.integ = integ = 1
		self.beat = beat = 1

		##################################################
		# Blocks
		##################################################
		_magnitude_sizer = wx.BoxSizer(wx.VERTICAL)
		self._magnitude_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_magnitude_sizer,
			value=self.magnitude,
			callback=self.set_magnitude,
			label="Magnitude",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._magnitude_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_magnitude_sizer,
			value=self.magnitude,
			callback=self.set_magnitude,
			minimum=0.05,
			maximum=0.5,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_magnitude_sizer)
		_integ_sizer = wx.BoxSizer(wx.VERTICAL)
		self._integ_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_integ_sizer,
			value=self.integ,
			callback=self.set_integ,
			label="Integration Time (Sec)",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._integ_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_integ_sizer,
			value=self.integ,
			callback=self.set_integ,
			minimum=1,
			maximum=30,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_integ_sizer)
		_beat_sizer = wx.BoxSizer(wx.VERTICAL)
		self._beat_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_beat_sizer,
			value=self.beat,
			callback=self.set_beat,
			label="Beat Frequency (kHz)",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._beat_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_beat_sizer,
			value=self.beat,
			callback=self.set_beat,
			minimum=1,
			maximum=10,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_beat_sizer)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="2nd detector power level",
			sample_rate=2,
			v_scale=0,
			v_offset=0,
			t_scale=450,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_STRIPCHART,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate/10,
			fft_size=1024,
			fft_rate=8,
			average=True,
			avg_alpha=0.1,
			title="First Detector Spectrum",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(1.0/((samp_rate/10)*integ), 1)
		self.low_pass_filter_0 = gr.fir_filter_fff(int(samp_rate/25e3), firdes.low_pass(
			1, samp_rate, 11e3, 2.5e3, firdes.WIN_HAMMING, 6.76))
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_float*1, samp_rate)
		self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
		self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(samp_rate/20))
		self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
		self.blocks_add_xx_0 = blocks.add_vcc(1)
		self.band_pass_filter_0 = gr.fir_filter_fff(1, firdes.band_pass(
			1, samp_rate/10, (beat*1000)-100, (beat*1000)+100, 50, firdes.WIN_HAMMING, 6.76))
		self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 122e3, magnitude, 0)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 122e3-(beat*1000), magnitude, 0)
		self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, 0.2, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 2))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_add_xx_0, 1))
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
		self.connect((self.blocks_add_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
		self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.band_pass_filter_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))
		self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 1))
		self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.blocks_multiply_xx_0, 0), (self.single_pole_iir_filter_xx_0, 0))
		self.connect((self.blocks_keep_one_in_n_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_keep_one_in_n_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, 11e3, 2.5e3, firdes.WIN_HAMMING, 6.76))
		self.blocks_throttle_0.set_sample_rate(self.samp_rate)
		self.blocks_keep_one_in_n_0.set_n(int(self.samp_rate/20))
		self.single_pole_iir_filter_xx_0.set_taps(1.0/((self.samp_rate/10)*self.integ))
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate/10, (self.beat*1000)-100, (self.beat*1000)+100, 50, firdes.WIN_HAMMING, 6.76))
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate/10)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)

	def get_magnitude(self):
		return self.magnitude

	def set_magnitude(self, magnitude):
		self.magnitude = magnitude
		self._magnitude_slider.set_value(self.magnitude)
		self._magnitude_text_box.set_value(self.magnitude)
		self.analog_sig_source_x_0.set_amplitude(self.magnitude)
		self.analog_sig_source_x_0_0.set_amplitude(self.magnitude)

	def get_integ(self):
		return self.integ

	def set_integ(self, integ):
		self.integ = integ
		self._integ_slider.set_value(self.integ)
		self._integ_text_box.set_value(self.integ)
		self.single_pole_iir_filter_xx_0.set_taps(1.0/((self.samp_rate/10)*self.integ))

	def get_beat(self):
		return self.beat

	def set_beat(self, beat):
		self.beat = beat
		self._beat_slider.set_value(self.beat)
		self._beat_text_box.set_value(self.beat)
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.samp_rate/10, (self.beat*1000)-100, (self.beat*1000)+100, 50, firdes.WIN_HAMMING, 6.76))
		self.analog_sig_source_x_0.set_frequency(122e3-(self.beat*1000))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = intensity_interferometer()
	tb.Run(True)

