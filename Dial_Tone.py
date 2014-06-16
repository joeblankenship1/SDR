#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Dial Tone
# Generated: Sat May 24 22:11:41 2014
##################################################

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class Dial_Tone(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Dial Tone")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.src_freq_1 = src_freq_1 = 350
		self.samp_rate = samp_rate = 32000
		self.noise_amp = noise_amp = .005
		self.Src_freq_2 = Src_freq_2 = 440

		##################################################
		# Blocks
		##################################################
		_src_freq_1_sizer = wx.BoxSizer(wx.VERTICAL)
		self._src_freq_1_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_src_freq_1_sizer,
			value=self.src_freq_1,
			callback=self.set_src_freq_1,
			label="Src_Freq_1",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._src_freq_1_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_src_freq_1_sizer,
			value=self.src_freq_1,
			callback=self.set_src_freq_1,
			minimum=0,
			maximum=1000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_src_freq_1_sizer)
		_noise_amp_sizer = wx.BoxSizer(wx.VERTICAL)
		self._noise_amp_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_noise_amp_sizer,
			value=self.noise_amp,
			callback=self.set_noise_amp,
			label="noise_amp",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._noise_amp_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_noise_amp_sizer,
			value=self.noise_amp,
			callback=self.set_noise_amp,
			minimum=0,
			maximum=0.1,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_noise_amp_sizer)
		_Src_freq_2_sizer = wx.BoxSizer(wx.VERTICAL)
		self._Src_freq_2_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_Src_freq_2_sizer,
			value=self.Src_freq_2,
			callback=self.set_Src_freq_2,
			label="Src_Freq_2",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._Src_freq_2_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_Src_freq_2_sizer,
			value=self.Src_freq_2,
			callback=self.set_Src_freq_2,
			minimum=0,
			maximum=1000,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_Src_freq_2_sizer)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		self.blocks_add_xx_0 = blocks.add_vff(1)
		self.audio_sink_0 = audio.sink(48000, "", True)
		self.analog_sig_source_x_1 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, Src_freq_2, 0.1, 0)
		self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_COS_WAVE, src_freq_1, .1, 0)
		self.analog_noise_source_x_0 = analog.noise_source_f(analog.GR_GAUSSIAN, noise_amp, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_add_xx_0, 0))
		self.connect((self.analog_sig_source_x_1, 0), (self.blocks_add_xx_0, 1))
		self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 2))
		self.connect((self.blocks_add_xx_0, 0), (self.wxgui_scopesink2_0, 0))


	def get_src_freq_1(self):
		return self.src_freq_1

	def set_src_freq_1(self, src_freq_1):
		self.src_freq_1 = src_freq_1
		self.analog_sig_source_x_0.set_frequency(self.src_freq_1)
		self._src_freq_1_slider.set_value(self.src_freq_1)
		self._src_freq_1_text_box.set_value(self.src_freq_1)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_1.set_sampling_freq(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

	def get_noise_amp(self):
		return self.noise_amp

	def set_noise_amp(self, noise_amp):
		self.noise_amp = noise_amp
		self.analog_noise_source_x_0.set_amplitude(self.noise_amp)
		self._noise_amp_slider.set_value(self.noise_amp)
		self._noise_amp_text_box.set_value(self.noise_amp)

	def get_Src_freq_2(self):
		return self.Src_freq_2

	def set_Src_freq_2(self, Src_freq_2):
		self.Src_freq_2 = Src_freq_2
		self.analog_sig_source_x_1.set_frequency(self.Src_freq_2)
		self._Src_freq_2_slider.set_value(self.Src_freq_2)
		self._Src_freq_2_text_box.set_value(self.Src_freq_2)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = Dial_Tone()
	tb.Run(True)

