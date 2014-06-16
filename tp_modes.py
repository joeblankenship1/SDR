#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Tp Modes
# Generated: Thu Jan 23 20:31:21 2014
##################################################

from datetime import datetime
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
import baz
import wx

class tp_modes(grc_wxgui.top_block_gui):

	def __init__(self, ppm=30, srate=2.4e6, fftsize=8192):
		grc_wxgui.top_block_gui.__init__(self, title="Tp Modes")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Parameters
		##################################################
		self.ppm = ppm
		self.srate = srate
		self.fftsize = fftsize

		##################################################
		# Variables
		##################################################
		self.prefix = prefix = "/home/superkuh/vsrt_"
		self.recfile = recfile = prefix + datetime.now().strftime("%Y.%m.%d.%H.%M.%S") + ".log"
		self.freq = freq = 1600e6
		self.bp_width = bp_width = 30e3
		self.bp_low = bp_low = 90e3
		self.actual_lower_freq = actual_lower_freq = 10.7e9
		self.IF_lower_freq = IF_lower_freq = 950e6
		self.scope_rate = scope_rate = 2.0
		self.record = record = False
		self.realfreq_display = realfreq_display = actual_lower_freq + (freq - IF_lower_freq)
		self.integ = integ = 1
		self.capture_file = capture_file = recfile
		self.bp_high = bp_high = bp_low+bp_width

		##################################################
		# Blocks
		##################################################
		self._record_check_box = forms.check_box(
			parent=self.GetWin(),
			value=self.record,
			callback=self.set_record,
			label="Record",
			true=True,
			false=False,
		)
		self.GridAdd(self._record_check_box, 0, 1, 1, 1)
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
		self._capture_file_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.capture_file,
			callback=self.set_capture_file,
			label=" ",
			converter=forms.str_converter(),
		)
		self.GridAdd(self._capture_file_text_box, 0, 2, 1, 1)
		_bp_low_sizer = wx.BoxSizer(wx.VERTICAL)
		self._bp_low_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_bp_low_sizer,
			value=self.bp_low,
			callback=self.set_bp_low,
			label="Bandpass Low End",
			converter=forms.int_converter(),
			proportion=0,
		)
		self._bp_low_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_bp_low_sizer,
			value=self.bp_low,
			callback=self.set_bp_low,
			minimum=80e3,
			maximum=100e3,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=int,
			proportion=1,
		)
		self.Add(_bp_low_sizer)
		self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="count of LNBF beat frequency bins",
			sample_rate=scope_rate,
			v_scale=0,
			v_offset=0,
			t_scale=450,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_f(
			self.GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=srate,
			fft_size=2048,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="Total Power FFT Spectrum",
			peak_hold=False,
		)
		self.Add(self.wxgui_fftsink2_0.win)
		self.single_pole_iir_filter_xx_0 = filter.single_pole_iir_filter_ff(1.0/((srate/10)*integ), 1)
		self.rtl2832_source_0 = baz.rtl_source_c(defer_creation=True, output_size=gr.sizeof_gr_complex)
		self.rtl2832_source_0.set_verbose(True)
		self.rtl2832_source_0.set_vid(0x0)
		self.rtl2832_source_0.set_pid(0x0)
		self.rtl2832_source_0.set_tuner_name("r820t")
		self.rtl2832_source_0.set_default_timeout(0)
		self.rtl2832_source_0.set_use_buffer(True)
		self.rtl2832_source_0.set_fir_coefficients(([]))
		
		self.rtl2832_source_0.set_read_length(0)
		
		
		
		
		if self.rtl2832_source_0.create() == False: raise Exception("Failed to create RTL2832 Source: rtl2832_source_0")
		
		
		self.rtl2832_source_0.set_sample_rate(scope_rate)
		
		self.rtl2832_source_0.set_frequency(IF_lower_freq)
		
		
		
		self.rtl2832_source_0.set_auto_gain_mode(True)
		self.rtl2832_source_0.set_relative_gain(True)
		self.rtl2832_source_0.set_gain(0)
		  
		self._realfreq_display_static_text = forms.static_text(
			parent=self.GetWin(),
			value=self.realfreq_display,
			callback=self.set_realfreq_display,
			label="Actual Frequency",
			converter=forms.float_converter(),
		)
		self.GridAdd(self._realfreq_display_static_text, 0, 0, 1, 1)
		self.low_pass_filter_0 = gr.fir_filter_fff(int(srate/24e4), firdes.low_pass(
			1, srate, 200e3, 24e3, firdes.WIN_HAMMING, 6.76))
		_freq_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq_sizer,
			value=self.freq,
			callback=self.set_freq,
			label="Frequency",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq_sizer,
			value=self.freq,
			callback=self.set_freq,
			minimum=950e6,
			maximum=2150e6,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_freq_sizer)
		self._bp_width_text_box = forms.text_box(
			parent=self.GetWin(),
			value=self.bp_width,
			callback=self.set_bp_width,
			label="BP Width",
			converter=forms.int_converter(),
		)
		self.GridAdd(self._bp_width_text_box, 0, 4, 1, 1)
		self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
		self.blocks_keep_one_in_n_0 = blocks.keep_one_in_n(gr.sizeof_float*1, int(srate/20))
		self.blocks_file_sink_1 = blocks.file_sink(gr.sizeof_float*1, "/dev/null" if record == False else capture_file)
		self.blocks_file_sink_1.set_unbuffered(True)
		self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
		self.band_pass_filter_0 = gr.fir_filter_fff(1, firdes.band_pass(
			1, srate/5, bp_low, bp_high, 24e3, firdes.WIN_HAMMING, 6.76))

		##################################################
		# Connections
		##################################################
		self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 1))
		self.connect((self.band_pass_filter_0, 0), (self.blocks_multiply_xx_0, 0))
		self.connect((self.blocks_multiply_xx_0, 0), (self.single_pole_iir_filter_xx_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.band_pass_filter_0, 0))
		self.connect((self.single_pole_iir_filter_xx_0, 0), (self.blocks_keep_one_in_n_0, 0))
		self.connect((self.blocks_keep_one_in_n_0, 0), (self.wxgui_scopesink2_0_0, 0))
		self.connect((self.blocks_keep_one_in_n_0, 0), (self.blocks_file_sink_1, 0))
		self.connect((self.rtl2832_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))


	def get_ppm(self):
		return self.ppm

	def set_ppm(self, ppm):
		self.ppm = ppm

	def get_srate(self):
		return self.srate

	def set_srate(self, srate):
		self.srate = srate
		self.single_pole_iir_filter_xx_0.set_taps(1.0/((self.srate/10)*self.integ))
		self.blocks_keep_one_in_n_0.set_n(int(self.srate/20))
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.srate, 200e3, 24e3, firdes.WIN_HAMMING, 6.76))
		self.wxgui_fftsink2_0.set_sample_rate(self.srate)
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.srate/5, self.bp_low, self.bp_high, 24e3, firdes.WIN_HAMMING, 6.76))

	def get_fftsize(self):
		return self.fftsize

	def set_fftsize(self, fftsize):
		self.fftsize = fftsize

	def get_prefix(self):
		return self.prefix

	def set_prefix(self, prefix):
		self.prefix = prefix
		self.set_recfile(self.prefix + datetime.now().strftime("%Y.%m.%d.%H.%M.%S") + ".log")

	def get_recfile(self):
		return self.recfile

	def set_recfile(self, recfile):
		self.recfile = recfile
		self.set_capture_file(self.recfile)

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self.set_realfreq_display(self.actual_lower_freq + (self.freq - self.IF_lower_freq))
		self._freq_slider.set_value(self.freq)
		self._freq_text_box.set_value(self.freq)

	def get_bp_width(self):
		return self.bp_width

	def set_bp_width(self, bp_width):
		self.bp_width = bp_width
		self.set_bp_high(self.bp_low+self.bp_width)
		self._bp_width_text_box.set_value(self.bp_width)

	def get_bp_low(self):
		return self.bp_low

	def set_bp_low(self, bp_low):
		self.bp_low = bp_low
		self.set_bp_high(self.bp_low+self.bp_width)
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.srate/5, self.bp_low, self.bp_high, 24e3, firdes.WIN_HAMMING, 6.76))
		self._bp_low_slider.set_value(self.bp_low)
		self._bp_low_text_box.set_value(self.bp_low)

	def get_actual_lower_freq(self):
		return self.actual_lower_freq

	def set_actual_lower_freq(self, actual_lower_freq):
		self.actual_lower_freq = actual_lower_freq
		self.set_realfreq_display(self.actual_lower_freq + (self.freq - self.IF_lower_freq))

	def get_IF_lower_freq(self):
		return self.IF_lower_freq

	def set_IF_lower_freq(self, IF_lower_freq):
		self.IF_lower_freq = IF_lower_freq
		self.set_realfreq_display(self.actual_lower_freq + (self.freq - self.IF_lower_freq))
		self.rtl2832_source_0.set_frequency(self.IF_lower_freq)

	def get_scope_rate(self):
		return self.scope_rate

	def set_scope_rate(self, scope_rate):
		self.scope_rate = scope_rate
		self.wxgui_scopesink2_0_0.set_sample_rate(self.scope_rate)
		self.rtl2832_source_0.set_sample_rate(self.scope_rate)

	def get_record(self):
		return self.record

	def set_record(self, record):
		self.record = record
		self._record_check_box.set_value(self.record)
		self.blocks_file_sink_1.open("/dev/null" if self.record == False else self.capture_file)

	def get_realfreq_display(self):
		return self.realfreq_display

	def set_realfreq_display(self, realfreq_display):
		self.realfreq_display = realfreq_display
		self._realfreq_display_static_text.set_value(self.realfreq_display)

	def get_integ(self):
		return self.integ

	def set_integ(self, integ):
		self.integ = integ
		self._integ_slider.set_value(self.integ)
		self._integ_text_box.set_value(self.integ)
		self.single_pole_iir_filter_xx_0.set_taps(1.0/((self.srate/10)*self.integ))

	def get_capture_file(self):
		return self.capture_file

	def set_capture_file(self, capture_file):
		self.capture_file = capture_file
		self._capture_file_text_box.set_value(self.capture_file)
		self.blocks_file_sink_1.open("/dev/null" if self.record == False else self.capture_file)

	def get_bp_high(self):
		return self.bp_high

	def set_bp_high(self, bp_high):
		self.bp_high = bp_high
		self.band_pass_filter_0.set_taps(firdes.band_pass(1, self.srate/5, self.bp_low, self.bp_high, 24e3, firdes.WIN_HAMMING, 6.76))

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	parser.add_option("", "--ppm", dest="ppm", type="eng_float", default=eng_notation.num_to_str(30),
		help="Set ppm error [default=%default]")
	parser.add_option("", "--srate", dest="srate", type="eng_float", default=eng_notation.num_to_str(2.4e6),
		help="Set Sample Rate [default=%default]")
	parser.add_option("", "--fftsize", dest="fftsize", type="intx", default=8192,
		help="Set fftsize [default=%default]")
	(options, args) = parser.parse_args()
	tb = tp_modes(ppm=options.ppm, srate=options.srate, fftsize=options.fftsize)
	tb.Run(True)

