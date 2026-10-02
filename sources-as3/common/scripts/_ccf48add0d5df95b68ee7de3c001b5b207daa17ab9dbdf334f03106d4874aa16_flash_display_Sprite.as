package
{
   import flash.display.Sprite;
   import flash.system.Security;
   
   [ExcludeClass]
   public class _ccf48add0d5df95b68ee7de3c001b5b207daa17ab9dbdf334f03106d4874aa16_flash_display_Sprite extends Sprite
   {
       
      
      public function _ccf48add0d5df95b68ee7de3c001b5b207daa17ab9dbdf334f03106d4874aa16_flash_display_Sprite()
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
