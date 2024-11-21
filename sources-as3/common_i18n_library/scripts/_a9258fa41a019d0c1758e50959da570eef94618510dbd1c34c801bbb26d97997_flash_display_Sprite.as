package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _a9258fa41a019d0c1758e50959da570eef94618510dbd1c34c801bbb26d97997_flash_display_Sprite extends Sprite
   {
       
      
      public function _a9258fa41a019d0c1758e50959da570eef94618510dbd1c34c801bbb26d97997_flash_display_Sprite()
      {
         super();
      }
      
      public function allowDomainInRSL(... rest) : void
      {
         Security.allowDomain.apply(null,rest);
      }
      
      public function allowInsecureDomainInRSL(... rest) : void
      {
         Security.allowInsecureDomain.apply(null,rest);
      }
   }
}
