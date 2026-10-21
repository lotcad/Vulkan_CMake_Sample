// 자동 생성 — 직접 고치지 말 것. 원본: LotCAD_API.h
// 생성기: tools/gen_csharp_binding.py (엔진 빌드의 SDK 내보내기 단계에서 Windows 일 때만 실행)

using System;
using System.Runtime.InteropServices;
using System.Text;

namespace LotCAD
{
    /// <summary>
    /// LotCAD C API (LotCAD_API.h) 선언. 함수 이름은 헤더와 같다. 영역별로 CadApi.&lt;영역&gt;.cs 에 나뉘어 있다.
    /// <para>콜백(delegate)을 넘길 땐 그 delegate 객체를 필드 등에 **붙잡아 두어야** 한다 —
    /// 지역 변수로만 두면 GC 가 거둬 엔진이 사라진 함수를 부르게 된다.</para>
    /// </summary>
    public static partial class CadApi
    {
        /// <summary>엔진 DLL 이름(LotCADCore.dll). exe 옆이나 PATH 에 있어야 한다.</summary>
        public const string Dll = "LotCADCore";

        /// <summary>
        /// 문자열을 버퍼로 돌려주는 함수(char* buf, int cap)를 읽는다. 예:
        /// <c>CadApi.Str((b, n) =&gt; CadApi.CAD_GetObjectJson(id, b, n))</c>.
        /// 반환이 음수면 null. 버퍼가 모자라 보이면(반환 ≥ cap−1) 키워 다시 부른다 —
        /// "필요한 길이" 를 돌려주는 함수와 "잘라 복사한 길이" 를 돌려주는 함수 둘 다 맞게 읽힌다.
        /// ⚠️ 부를 때 무언가를 **실행**하는 함수(2회 호출 규약)는 <see cref="StrOnce"/> — 여기선 두 번 실행될 수 있다.
        /// </summary>
        public static string Str(Func<byte[], int, int> getter, int initialCapacity = 256)
        {
            int cap = Math.Max(16, initialCapacity);
            while (true)
            {
                var buf = new byte[cap];
                int r = getter(buf, cap);
                if (r < 0) return null;
                if (r >= cap - 1 && cap < (1 << 26)) { cap = Math.Max(r + 1, cap * 2); continue; }
                int len = Array.IndexOf(buf, (byte)0);
                if (len < 0) len = cap;
                return Encoding.UTF8.GetString(buf, 0, len);
            }
        }

        /// <summary>
        /// **2회 호출 규약** 함수를 읽는다 — 헤더 주석에 "2회 호출" · "null 이면 길이만" 이라 적힌 것
        /// (해석 CAD_WindTunnel·CAD_Water·CAD_StructuralAnalysis, CAD_GetObjectJson, CAD_McpCall …).
        /// buf=null 로 길이를 물을 때 **한 번 실행**하고, 같은 인자로 버퍼를 주면 다시 실행하지 않고 그 결과를 준다.
        /// 이런 함수를 <see cref="Str"/> 로 읽으면 버퍼가 모자랄 때 다시 불러 **두 번 실행**된다(해석 start·run → "이미 도는 중").
        /// 예: <c>CadApi.StrOnce((b, n) =&gt; CadApi.CAD_WindTunnel(json, b, n))</c>. 실패(음수)면 null.
        /// </summary>
        public static string StrOnce(Func<byte[], int, int> getter)
        {
            int need = getter(null, 0);
            if (need < 0) return null;
            var buf = new byte[need + 1];
            if (getter(buf, buf.Length) < 0) return null;
            int len = Array.IndexOf(buf, (byte)0);
            if (len < 0) len = buf.Length;
            return Encoding.UTF8.GetString(buf, 0, len);
        }
    }

    /// <summary>
    /// string[] → UTF-8 문자열 포인터 배열(const char* const*). .NET 은 string[] 에 UTF-8 마샬링을 못 붙여서
    /// 직접 만든다. using 으로 감싸면 호출 뒤 해제된다. null 원소는 NULL 포인터.
    /// </summary>
    public sealed class Utf8StringArray : IDisposable
    {
        public IntPtr[] Pointers { get; private set; }

        public Utf8StringArray(string[] values)
        {
            Pointers = new IntPtr[values == null ? 0 : values.Length];
            for (int i = 0; i < Pointers.Length; i++)
                Pointers[i] = values[i] == null ? IntPtr.Zero : Marshal.StringToCoTaskMemUTF8(values[i]);
        }

        public void Dispose()
        {
            if (Pointers == null) return;
            foreach (var p in Pointers)
                if (p != IntPtr.Zero) Marshal.FreeCoTaskMem(p);
            Pointers = null;
        }
    }
}
