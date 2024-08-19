#pragma once

// 머신에서 Microsoft Visual C++를 사용하여 생성한 IDispatch 래퍼 클래스입니다.

// 참고: 이 파일의 콘텐츠를 수정하지 마세요. Microsoft Visual C++를 통해 이 클래스가 다시 생성될 경우 
// 수정 내용을 덮어씁니다.

/////////////////////////////////////////////////////////////////////////////

#include "afxwin.h"

class CSHINHANINDICTRL1 : public CWnd
{
protected:
	DECLARE_DYNCREATE(CSHINHANINDICTRL1)
public:
	CLSID const& GetClsid()
	{
		static CLSID const clsid
			= {0x6eed42cf,0xd977,0x475e,{0xae,0xdc,0xc2,0xba,0xc0,0x94,0xce,0x54}};
		return clsid;
	}
	virtual BOOL Create(LPCTSTR lpszClassName, LPCTSTR lpszWindowName, DWORD dwStyle,
						const RECT& rect, CWnd* pParentWnd, UINT nID, 
						CCreateContext* pContext = nullptr)
	{ 
		return CreateControl(GetClsid(), lpszWindowName, dwStyle, rect, pParentWnd, nID);
	}

	BOOL Create(LPCTSTR lpszWindowName, DWORD dwStyle, const RECT& rect, CWnd* pParentWnd,
				UINT nID, CFile* pPersist = nullptr, BOOL bStorage = FALSE,
				BSTR bstrLicKey = nullptr)
	{ 
		return CreateControl(GetClsid(), lpszWindowName, dwStyle, rect, pParentWnd, nID,
		pPersist, bStorage, bstrLicKey); 
	}

// 특성
public:


// 작업
public:
// _DshinhanINDI

// 함수
//

	BOOL SetSingleData(short index, VARIANT data)
	{
		BOOL result;
		static BYTE parms[] = VTS_I2 VTS_VARIANT;
		InvokeHelper(0x1, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, index, &data);
		return result;
	}
	BOOL SetMultiData(short row, short index, VARIANT data)
	{
		BOOL result;
		static BYTE parms[] = VTS_I2 VTS_I2 VTS_VARIANT;
		InvokeHelper(0x2, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, row, index, &data);
		return result;
	}
	BOOL SetQueryName(VARIANT name)
	{
		BOOL result;
		static BYTE parms[] = VTS_VARIANT;
		InvokeHelper(0x3, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, &name);
		return result;
	}
	VARIANT GetQueryName()
	{
		VARIANT result;
		InvokeHelper(0x4, DISPATCH_METHOD, VT_VARIANT, (void*)&result, nullptr);
		return result;
	}
	short RequestData()
	{
		short result;
		InvokeHelper(0x5, DISPATCH_METHOD, VT_I2, (void*)&result, nullptr);
		return result;
	}
	BOOL RequestRTReg(VARIANT type, VARIANT code)
	{
		BOOL result;
		static BYTE parms[] = VTS_VARIANT VTS_VARIANT;
		InvokeHelper(0x6, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, &type, &code);
		return result;
	}
	BOOL UnRequestRTReg(VARIANT type, VARIANT code)
	{
		BOOL result;
		static BYTE parms[] = VTS_VARIANT VTS_VARIANT;
		InvokeHelper(0x7, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, &type, &code);
		return result;
	}
	VARIANT GetSingleData(short index)
	{
		VARIANT result;
		static BYTE parms[] = VTS_I2;
		InvokeHelper(0x8, DISPATCH_METHOD, VT_VARIANT, (void*)&result, parms, index);
		return result;
	}
	VARIANT GetMultiData(short row, short index)
	{
		VARIANT result;
		static BYTE parms[] = VTS_I2 VTS_I2;
		InvokeHelper(0x9, DISPATCH_METHOD, VT_VARIANT, (void*)&result, parms, row, index);
		return result;
	}
	VARIANT GetSingleBlockData()
	{
		VARIANT result;
		InvokeHelper(0xA, DISPATCH_METHOD, VT_VARIANT, (void*)&result, nullptr);
		return result;
	}
	VARIANT GetMultiBlockData()
	{
		VARIANT result;
		InvokeHelper(0xB, DISPATCH_METHOD, VT_VARIANT, (void*)&result, nullptr);
		return result;
	}
	short GetSingleRowCount()
	{
		short result;
		InvokeHelper(0xC, DISPATCH_METHOD, VT_I2, (void*)&result, nullptr);
		return result;
	}
	short GetMultiRowCount()
	{
		short result;
		InvokeHelper(0xD, DISPATCH_METHOD, VT_I2, (void*)&result, nullptr);
		return result;
	}
	short GetErrorState()
	{
		short result;
		InvokeHelper(0xE, DISPATCH_METHOD, VT_I2, (void*)&result, nullptr);
		return result;
	}
	VARIANT GetErrorCode()
	{
		VARIANT result;
		InvokeHelper(0xF, DISPATCH_METHOD, VT_VARIANT, (void*)&result, nullptr);
		return result;
	}
	VARIANT GetErrorMessage()
	{
		VARIANT result;
		InvokeHelper(0x10, DISPATCH_METHOD, VT_VARIANT, (void*)&result, nullptr);
		return result;
	}
	short GetCommState()
	{
		short result;
		InvokeHelper(0x11, DISPATCH_METHOD, VT_I2, (void*)&result, nullptr);
		return result;
	}
	BOOL UnRequestRTRegAll()
	{
		BOOL result;
		InvokeHelper(0x12, DISPATCH_METHOD, VT_BOOL, (void*)&result, nullptr);
		return result;
	}
	void SetRQCount(short nRqCount)
	{
		static BYTE parms[] = VTS_I2;
		InvokeHelper(0x13, DISPATCH_METHOD, VT_EMPTY, nullptr, parms, nRqCount);
	}
	void ClearReceiveBuffer()
	{
		InvokeHelper(0x14, DISPATCH_METHOD, VT_EMPTY, nullptr, nullptr);
	}
	void SelfMemFree(BOOL bSelfMemFree)
	{
		static BYTE parms[] = VTS_BOOL;
		InvokeHelper(0x15, DISPATCH_METHOD, VT_EMPTY, nullptr, parms, bSelfMemFree);
	}
	BOOL SetID(VARIANT name)
	{
		BOOL result;
		static BYTE parms[] = VTS_VARIANT;
		InvokeHelper(0x16, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, &name);
		return result;
	}
	VARIANT GetCodeByName(VARIANT name)
	{
		VARIANT result;
		static BYTE parms[] = VTS_VARIANT;
		InvokeHelper(0x17, DISPATCH_METHOD, VT_VARIANT, (void*)&result, parms, &name);
		return result;
	}
	BOOL SetSingleEncData(short index, VARIANT data)
	{
		BOOL result;
		static BYTE parms[] = VTS_I2 VTS_VARIANT;
		InvokeHelper(0x18, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, index, &data);
		return result;
	}
	BOOL StartIndi(VARIANT id, VARIANT pswd, VARIANT authpswd, VARIANT path)
	{
		BOOL result;
		static BYTE parms[] = VTS_VARIANT VTS_VARIANT VTS_VARIANT VTS_VARIANT;
		InvokeHelper(0x19, DISPATCH_METHOD, VT_BOOL, (void*)&result, parms, &id, &pswd, &authpswd, &path);
		return result;
	}
	BOOL CloseIndi()
	{
		BOOL result;
		InvokeHelper(0x1A, DISPATCH_METHOD, VT_BOOL, (void*)&result, nullptr);
		return result;
	}
	VARIANT GetInputSingleData(short rqid, short index)
	{
		VARIANT result;
		static BYTE parms[] = VTS_I2 VTS_I2;
		InvokeHelper(0x1B, DISPATCH_METHOD, VT_VARIANT, (void*)&result, parms, rqid, index);
		return result;
	}
	VARIANT GetInputMultiData(short rqid, short row, short index)
	{
		VARIANT result;
		static BYTE parms[] = VTS_I2 VTS_I2 VTS_I2;
		InvokeHelper(0x1C, DISPATCH_METHOD, VT_VARIANT, (void*)&result, parms, rqid, row, index);
		return result;
	}
	VARIANT GetInputTRName(short rqid)
	{
		VARIANT result;
		static BYTE parms[] = VTS_I2;
		InvokeHelper(0x1D, DISPATCH_METHOD, VT_VARIANT, (void*)&result, parms, rqid);
		return result;
	}
	void AboutBox()
	{
		InvokeHelper(0xFFFFFDD8, DISPATCH_METHOD, VT_EMPTY, nullptr, nullptr);
	}

// 속성
//

// _DshinhanINDIEvents

// 함수
//

	void ReceiveData(short rqid)
	{
		static BYTE parms[] = VTS_I2;
		InvokeHelper(0x1, DISPATCH_METHOD, VT_EMPTY, nullptr, parms, rqid);
	}
	void ReceiveRTData(VARIANT rttype)
	{
		static BYTE parms[] = VTS_VARIANT;
		InvokeHelper(0x2, DISPATCH_METHOD, VT_EMPTY, nullptr, parms, &rttype);
	}
	void ReceiveSysMsg(short nMsgID)
	{
		static BYTE parms[] = VTS_I2;
		InvokeHelper(0x3, DISPATCH_METHOD, VT_EMPTY, nullptr, parms, nMsgID);
	}

// 속성
//



};
