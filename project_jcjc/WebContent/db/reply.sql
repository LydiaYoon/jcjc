drop table reply;

drop sequence seq_reply;

create table reply (
	reply_no number primary key,
	post_no number not null,
	user_id varchar2(20) not null,
	reply_content clob not null,
	reply_date date not null,
	constraint reply_no_const foreign key (post_no) references post(post_no) on delete cascade
);

create sequence seq_reply
increment by 1
start with 1
nocycle
nocache;

insert into reply values(seq_reply.nextval, 1, '11', 
'인생에 가치를 주는 원질이 되는 것이다 그들은 앞이 긴지라 착목한는 곳이 원대하고 그들은 피가 더운지라 실현에 대한 자신과 용기가 있다',
'2001-01-01');
insert into reply values(seq_reply.nextval, 1, '22', 
'뭇 별과 같이 산야에 피어나는 군영과 같이 이상은 실로 인간의 부패를 방지하는 소금이라 할지니 인생에 가치를 주는 원질이 되는 것이다 그들은 앞이 긴지라 착목한는 곳이 원대하고 그들은 피가 더운지라 실현에 대한 자신과',
'2002-02-02');
insert into reply values(seq_reply.nextval, 1, '33', 
'그러므로 그들은 이상의 보배를 능히 품으며 그들의 이상은 아름답고 소담스러운 열매를 맺어',
'2003-03-03');
insert into reply values(seq_reply.nextval, 1, 'narae', 
'철환하였는가? 밥을 위하여서 옷을 위하여서 미인을 구하기 위하여서 그리하였는가? 아니다 그들은 커다란 이상 곧 만천하의 대중을 품에 안고 그들에게 밝은 길을 찾아 주며 그들을 행복스럽고 평화스러운 곳으로 인도하겠다는 커다란 이상을 품었기 때문이다',
'2003-03-03');

insert into reply values(seq_reply.nextval, 2, '44', 
'낙원을 장식하는 천자만홍이 어디 있으며 인생을 풍부하게 하는 온갖 과실이 어디 있으랴? 이상! 우리의 청춘이 가장 많이 품고 있는 이상! 이것이야말로 무한한 가치를 가진 것이다 사람은 크고 작고 간에 이상이 있음으로써 용감하고',
'2004-04-04');
insert into reply values(seq_reply.nextval, 2, '55', 
'인류의 역사를 꾸며 내려온 동력은 바로 이것이다 이성은 투명하되 얼음과 같으며 지혜는 날카로우나 갑 속에 든 칼이다',
'2005-05-05');
insert into reply values(seq_reply.nextval, 2, '66', 
'청춘의 끓는 피가 아니더면 인간이 얼마나 쓸쓸하랴? 얼음에 싸인 만물은 얼음이 있을 뿐이다 그들에게 생명을',
'2006-06-06');
insert into reply values(seq_reply.nextval, 2, '77', 
'길지 아니한 목숨을 사는가 싶이 살았으며 그들의 그림자는 천고에 사라지지 않는 것이다 이것은 현저하게 일월과 같은 예가 되려니와 그와 같지 못하다 할지라도 창공에 반짝이는 뭇 별과 같이 산야에 피어나는 군영과 같이 이상은','2007-07-07');

insert into reply values(seq_reply.nextval, 4, '11', 
'미인을 구하기 위하여서 그리하였는가? 아니다 그들은 커다란 이상 곧 만천하의 대중을 품에 안고 그들에게 밝은 길을 찾아 주며',
'2004-04-04');
insert into reply values(seq_reply.nextval, 4, '22', 
'그들을 행복스럽고 평화스러운 곳으로 인도하겠다는 커다란 이상을 품었기 때문이다 그러므로 그들은 길지 아니한 목숨을',
'2005-05-05');
insert into reply values(seq_reply.nextval, 5, '33', 
'청춘! 이는 듣기만 하여도 가슴이 설레는 말이다 청춘! 너의 두손을 가슴에 대고 물방아 같은 심장의 고동을 들어 보라 청춘의 피는 끓는다 끓는 피에 뛰노는 심장은 거선의 기관과 같이 힘있다 이것이다 인류의 역사를',
'2006-06-06');
insert into reply values(seq_reply.nextval, 5, '44', 
'이상은 실로 인간의 부패를 방지하는 소금이라 할지니 인생에 가치를 주는 원질이 되는 것이다 그들은 앞이 긴지라 착목한는 곳이 원대하고 그들은 피가 더운지라 실현에 대한 자신과 용기가 있다 그러므로 그들은 이상의 보배를 능히',
'2007-07-07');


commit
select * from reply;

insert into reply values(seq_reply.nextval, 8, '454', '454', '2000-01-01');
delete from reply where reply_no =1;
select * from reply order by reply_no;

update reply set reply_content='99999999', reply_date='2020-09-09' where reply_no= 5;

