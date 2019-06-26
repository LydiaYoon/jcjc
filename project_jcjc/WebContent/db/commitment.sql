drop table commitment;

drop sequence seq_commitment;

create table commitment(
	commitment_no number primary key,
	politician_no number not null,
	commitment_proposal_date date not null,
	commitment_title varchar2(100) not null,
	commitment_content clob not null,
	commitment_fulfillment varchar2(100) not null,
	constraint commitment_no_const foreign key (politician_no) references politician(politician_no) on delete cascade
);

create sequence seq_commitment
increment by 1
start with 1
nocycle
nocache;

insert into commitment values(
seq_commitment.nextval, 0, '2019-01-01', 
'데이터 분석',
'Hive<br>
- 데이터웨어하우징용 솔루션<br>
- 페이스북에서 개발. 현재 아파치 프로젝트에 속함<br>
- SQL과 매우 유사한 HiveQL 쿼리 제공 (내부적으로 맵리듀스 칩으로 변환되어 실행됨)<br>
- 자바를 모르는 데이터 분석가들도 쉽게 하둡 데이터를 분석할 수 있게 도와줌<br>
- 짧은 임시쿼리보다는 일괄적인 맵리듀스 처리에 이상적임', '이행'
);

insert into commitment values(
seq_commitment.nextval, 0, '2019-02-02', 
'비정형 데이터 수집',
'Flume<br>
- Chukwa 처럼 분산된 서버에 에이전트가 설치되고, 에이전트로부터 데이터를 전달받는 콜렉터로 구성<br>
- 전체 데이터의 흐름을 관리하는 마스터 서버가 있음<br>
- 즉, 데이터를 어디서 수집, 어떤 방식으로 전송, 어디에 저장할 지를 동적으로 변경할 수 있음 (클라우데라 개발)<br>', '진행'
);

insert into commitment values(
seq_commitment.nextval, 0, '2019-03-03', 
'정형 데이터 수집',
'Sqoop<br>
- 대용량 데이터 전송 솔루션<br>
- HDFS, RDBMS, DW, NoSQL 등 다양한 저장소에 대용량 데이터를 신속하게 전송할 수 있는 방법 제공<br>
- 상용 RDBMS도 지원하고, MySQL, PostareSQL 오픈소스 RDBMS도 지원함', '미이행'
);

insert into commitment values(
seq_commitment.nextval, 0, '2001-01-01',
'하둡 분산 파일 시스템',
'HDFS<br>
- 구글의 GFS를 기반으로 함<br>
- 수십 테라바이트 또는 페타바이트 이상의 대용량 파일을 분산된 서버에 저장하고,<br>
&nbsp;&nbsp;많은 클라이언트가 저장된 데이터를 빠르게 처리할 수 있게 설계된 파일 시스템<br>
- 저사양 서버를 이용해 스토리지를 구성할 수 있음<br>
- 대규모 데이터를 저장, 배치로 처리하는 경우', '진행');

insert into commitment values(
seq_commitment.nextval, 0, '2002-02-02',
'맵리듀스',
'MapReduce<br>
- HDFS에 분산 저장된 데이터에 스트리밍 접근을 요청하여 빠르게 분산 처리하도록 고안된 프로그래밍 모델, 이를 지원하는 시스템<br>
- 대규모 분산 컴퓨팅 혹은 단일 컴퓨팅 환경에서 개발자가 대량의 데이터를 병렬로 분석할 수 있음<br>
- 배치 데이터 처리에 적합<br>
- 개발자는 맵리듀스 알고리즘에 맞게 분석 프로그램을 개발하고,<br>
&nbsp;&nbsp;데이터의 입출력과 병렬 처리 등 기반 작업은 프레임워크가 알아서 처리해줌', '이행');

insert into commitment values(
seq_commitment.nextval, 0, '2003-03-03',
'Hadoop 클러스터 구축을 위한 준비',
'Hadoop 클러스터는 2가지의 노드 타입으로 구성<br>
- NameNode / JobTracker (Secondary NameNode)<br>
- DataNode / TaskTracker', '미이행');





insert into commitment values(
seq_commitment.nextval, 9770084, '2019-04-04',
'첫번째 테스트 제목', '첫번째 테스트 내용', '진행');

insert into commitment values(
seq_commitment.nextval, 9770084, '2019-05-05',
'두번째 테스트 제목', '두번째 테스트 내용', '진행');

insert into commitment values(
seq_commitment.nextval, 9770084, '2019-06-06',
'세번째 테스트 제목', '세번째 테스트 내용', '미이행');



insert into commitment values(
seq_commitment.nextval, 9770090, '2019-04-04',
'첫번째 테스트 제목', '첫번째 테스트 내용', '진행');

insert into commitment values(
seq_commitment.nextval, 9770090, '2019-05-05',
'두번째 테스트 제목', '두번째 테스트 내용', '진행');

insert into commitment values(
seq_commitment.nextval, 9770090, '2019-06-06',
'세번째 테스트 제목', '세번째 테스트 내용', '미이행');


insert into commitment values(
seq_commitment.nextval, 9770138, '2019-04-04',
'첫번째 테스트 제목', '첫번째 테스트 내용', '진행');

insert into commitment values(
seq_commitment.nextval, 9770138, '2019-05-05',
'두번째 테스트 제목', '두번째 테스트 내용', '이행');

insert into commitment values(
seq_commitment.nextval, 9770138, '2019-06-06',
'세번째 테스트 제목', '세번째 테스트 내용', '미이행');


select * from commitment order by commitment_no;

delete from commitment where commitment_no = 1;

update commitment set 
commitment_title = '999999', commitment_content = '999999', commitment_fulfillment = '진행' 
where commitment_no = 999;
