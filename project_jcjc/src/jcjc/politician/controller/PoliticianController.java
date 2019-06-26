package jcjc.politician.controller;

import java.util.List;

import javax.servlet.http.HttpSession;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import jcjc.commitment.entity.Commitment;
import jcjc.politician.biz.PoliticianBiz;
import jcjc.politician.entity.Politician;

@Controller("politicianController")
public class PoliticianController {

	@Autowired
	private PoliticianBiz biz;
	
	//all
	@RequestMapping("/politician/all.do")
	public ModelAndView politicianAll() {
		List<Politician> all = biz.selectAllPolitician();
		return new ModelAndView("politician/all", "all", all);
	}

	
	
	///////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////////
	///////////////////////////////////////////////////////////////////
	// 페이지 이동
	
	@RequestMapping("/politician/type.do")
	public ModelAndView selectType() {
		return new ModelAndView("politician/type");
	}
	
	@RequestMapping("/politician/location.do")
	public ModelAndView selectLocation() {
		return new ModelAndView("politician/location");
	}
	
	@RequestMapping("/politician/matching.do")
	public ModelAndView politicianMatching(HttpSession session) {
		Politician entity = (Politician) session.getAttribute("politician");
		return new ModelAndView("politician/matching");
	}
	
	
	
	////////////////////////////////////////////////
	////////////////////////////////////////////////
	////////////////////////////////////////////////
	
	@RequestMapping("/politician/prediction.do")
	public ModelAndView prediction(@RequestParam("politician_no") int politician_no, HttpSession session) {
		Politician politician = biz.findPolitian(politician_no);
		session.setAttribute("politician",  politician);
		return new ModelAndView("politician/prediction", "politician", politician);
	}
	

	@RequestMapping("/politician/profile.do")
	public ModelAndView profile(HttpSession session) {
		Politician entity = (Politician) session.getAttribute("politician");
		Politician politician = biz.findPolitian(entity.getPolitician_no());
		return new ModelAndView("politician/profile", "politician", politician);
	}

	
	
	////////////////////////////////////////////////
	////////////////////////////////////////////////
	////////////////////////////////////////////////
	// 회원 가입 시 호출하는 부분
	
	// [politiciuser_prefer_politician]
	@RequestMapping("/politician/prefer.do")
	public ModelAndView preferPoliticianList() {
		List<Politician> politician = biz.selectAllPolitician();
		return new ModelAndView("/user/preferpolitician", "politician", politician);
	}
	
	// [politiciuser_support_politician]
	@RequestMapping("/politician/support.do")
	public ModelAndView supportPoliticianList() {
		List<Politician> politician = biz.selectAllPolitician();
		return new ModelAndView("/user/supportpolitician", "politician", politician);
	}
	
	
	// [필터링 미구현 상태...]
	@RequestMapping(value = "/politician/search.do", method = RequestMethod.GET)
	public ModelAndView searchPolitician(@RequestParam("findpolitician") String findpolitician) {
		List<Politician> politician = biz.searchPolitician(findpolitician);
		return new ModelAndView("/user/searchpolitician", "politician", politician);
	}
	
}
